from PIL import Image
import numpy as np
from sklearn.cluster import MiniBatchKMeans
import webcolors
import math


def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % tuple(int(v) for v in rgb)


def closest_color_name(rgb):
    rgb = tuple(int(v) for v in rgb)

    # Try exact CSS3 name first
    try:
        return webcolors.rgb_to_name(rgb)
    except ValueError:
        pass

    # Build color mapping based on webcolors version
    # New versions (1.12+) use CSS3 enum with .names() method
    if hasattr(webcolors, 'CSS3') and hasattr(webcolors.CSS3, 'names'):
        name_to_hex = {name: webcolors.name_to_hex(name) for name in webcolors.CSS3.names}
    # Older versions with CSS3_NAMES_TO_HEX dict
    elif hasattr(webcolors, 'CSS3_NAMES_TO_HEX'):
        name_to_hex = webcolors.CSS3_NAMES_TO_HEX
    # Even older versions with CSS3_HEX_TO_NAMES
    elif hasattr(webcolors, 'CSS3_HEX_TO_NAMES'):
        name_to_hex = {v: k for k, v in webcolors.CSS3_HEX_TO_NAMES.items()}
    else:
        # Fallback: use a basic set of common colors
        name_to_hex = {
            'black': '#000000', 'white': '#ffffff', 'red': '#ff0000',
            'green': '#008000', 'blue': '#0000ff', 'yellow': '#ffff00',
            'cyan': '#00ffff', 'magenta': '#ff00ff', 'gray': '#808080',
            'silver': '#c0c0c0', 'maroon': '#800000', 'olive': '#808000',
            'navy': '#000080', 'purple': '#800080', 'teal': '#008080',
            'orange': '#ffa500', 'pink': '#ffc0cb', 'brown': '#a52a2a'
        }

    # Find closest color by Euclidean distance
    closest_name = None
    min_dist = float("inf")

    for name, hex_code in name_to_hex.items():
        r, g, b = webcolors.hex_to_rgb(hex_code)
        dist = ((r - rgb[0]) ** 2 +
                (g - rgb[1]) ** 2 +
                (b - rgb[2]) ** 2)

        if dist < min_dist:
            min_dist = dist
            closest_name = name

    return closest_name




def relative_luminance(rgb):
    def channel(c):
        c = c / 255.0
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4

    r, g, b = rgb
    return 0.2126 * channel(r) + 0.7152 * channel(g) + 0.0722 * channel(b)


def contrast_ratio(rgb1, rgb2):
    l1 = relative_luminance(rgb1)
    l2 = relative_luminance(rgb2)
    lighter = max(l1, l2)
    darker = min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)


def analyze_image_colors(image_path, num_colors=5, resize_max=800):
    img = Image.open(image_path).convert("RGB")
    w, h = img.size

    # Resize for speed
    max_dim = max(w, h)
    if max_dim > resize_max:
        scale = resize_max / max_dim
        img = img.resize((int(w * scale), int(h * scale)), Image.LANCZOS)

    arr = np.array(img)
    pixels = arr.reshape(-1, 3)

    # Sampling for faster clustering
    sample_size = 100000
    if len(pixels) > sample_size:
        idx = np.random.choice(len(pixels), sample_size, replace=False)
        sample = pixels[idx]
    else:
        sample = pixels

    kmeans = MiniBatchKMeans(n_clusters=num_colors, random_state=42)
    kmeans.fit(sample)
    centers = kmeans.cluster_centers_.astype(int)

    # Assign all pixels to nearest cluster
    from sklearn.metrics import pairwise_distances_argmin
    full_labels = pairwise_distances_argmin(pixels, centers)
    counts = np.bincount(full_labels, minlength=num_colors)
    percentages = counts / counts.sum()

    # Sort by dominance
    order = np.argsort(-percentages)

    colors = []
    for i in order:
        rgb = tuple(int(v) for v in centers[i])
        colors.append({
            "rgb": rgb,
            "hex": rgb_to_hex(rgb),
            "name": closest_color_name(rgb),
            "percent": float(percentages[i])
        })

    # Background from corners
    corners = [arr[0, 0], arr[0, -1], arr[-1, 0], arr[-1, -1]]
    corner_mean = tuple(np.mean(corners, axis=0).astype(int))
    bg_hex = rgb_to_hex(corner_mean)
    bg_name = closest_color_name(corner_mean)

    # Text color suggestion
    black = (0, 0, 0)
    white = (255, 255, 255)

    cr_black = contrast_ratio(corner_mean, black)
    cr_white = contrast_ratio(corner_mean, white)

    text_color = "#000000" if cr_black >= cr_white else "#ffffff"

    # Pick theme colors
    def dist(c1, c2):
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(c1, c2)))

    primary = None
    for c in colors:
        if dist(c["rgb"], corner_mean) > 30:
            primary = c
            break
    if not primary:
        primary = colors[0]

    secondary = colors[1] if len(colors) > 1 else primary
    accent = colors[2] if len(colors) > 2 else secondary

    # Theme name
    lumi = relative_luminance(corner_mean)
    mode = "dark" if lumi < 0.5 else "light"
    theme_name = f"{mode} - {primary['name']} primary"

    return {
        "primary": primary,
        "secondary": secondary,
        "accent": accent,
        "background": {"rgb": corner_mean, "hex": bg_hex, "name": bg_name},
        "text_on_background": text_color,
        "theme_name": theme_name,
        "palette": colors
    }
