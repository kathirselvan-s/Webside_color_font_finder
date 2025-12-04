from PIL import Image, ImageFilter, ImageOps
import numpy as np

# Try to import pytesseract, but make it optional
try:
    import pytesseract
    TESSERACT_AVAILABLE = True
except ImportError:
    TESSERACT_AVAILABLE = False


def analyze_font_styles(image_path):
    """
    Analyze font characteristics from a screenshot.
    Returns detected font styles and recommendations.
    """
    img = Image.open(image_path).convert("RGB")
    width, height = img.size
    
    # Initialize results
    font_data = {
        "detected_sizes": [],
        "heading_size": "32px",
        "body_size": "16px", 
        "small_size": "12px",
        "line_height": "1.5",
        "font_weight": "normal",
        "has_bold": False,
        "text_samples": [],
        "recommended_fonts": {
            "heading": "Inter, system-ui, sans-serif",
            "body": "Inter, system-ui, sans-serif",
            "monospace": "JetBrains Mono, Consolas, monospace"
        },
        "font_style": "sans-serif"  # Default assumption for modern websites
    }
    
    if TESSERACT_AVAILABLE:
        try:
            # Use pytesseract to get text data with bounding boxes
            data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)
            
            heights = []
            text_samples = []
            
            for i, text in enumerate(data['text']):
                if text.strip() and data['conf'][i] > 50:  # Confidence threshold
                    h = data['height'][i]
                    if h > 5:  # Filter noise
                        heights.append(h)
                        if len(text_samples) < 5 and len(text) > 3:
                            text_samples.append(text.strip())
            
            if heights:
                heights = np.array(heights)
                # Estimate font sizes based on text heights
                avg_height = np.median(heights)
                max_height = np.max(heights)
                min_height = np.min(heights)
                
                # Convert pixel heights to approximate font sizes
                font_data["body_size"] = f"{int(avg_height * 0.75)}px"
                font_data["heading_size"] = f"{int(max_height * 0.75)}px"
                font_data["small_size"] = f"{max(10, int(min_height * 0.75))}px"
                font_data["detected_sizes"] = sorted(list(set([int(h * 0.75) for h in heights if h > 8])))[:6]
                font_data["text_samples"] = text_samples
                
        except Exception as e:
            # Tesseract not configured or other error
            pass
    
    # Analyze image for font style hints
    font_data["font_style"] = _detect_font_style(img)
    font_data["has_bold"] = _detect_bold_text(img)
    
    # Update recommendations based on detected style
    if font_data["font_style"] == "serif":
        font_data["recommended_fonts"]["heading"] = "Playfair Display, Georgia, serif"
        font_data["recommended_fonts"]["body"] = "Merriweather, Georgia, serif"
    elif font_data["font_style"] == "monospace":
        font_data["recommended_fonts"]["heading"] = "JetBrains Mono, Consolas, monospace"
        font_data["recommended_fonts"]["body"] = "JetBrains Mono, Consolas, monospace"
    
    if font_data["has_bold"]:
        font_data["font_weight"] = "bold"
    
    return font_data


def _detect_font_style(img):
    """Detect if font appears to be serif, sans-serif, or monospace."""
    # Convert to grayscale and detect edges
    gray = img.convert('L')
    edges = gray.filter(ImageFilter.FIND_EDGES)
    edge_array = np.array(edges)
    
    # High edge density in text areas might indicate serif fonts
    edge_density = np.mean(edge_array > 50)
    
    # This is a heuristic - serif fonts tend to have more edge detail
    if edge_density > 0.15:
        return "serif"
    return "sans-serif"


def _detect_bold_text(img):
    """Detect if there's significant bold text in the image."""
    gray = img.convert('L')
    # Bold text has thicker strokes
    threshold = gray.point(lambda x: 0 if x < 128 else 255, '1')
    dark_pixels = np.array(threshold)
    
    # Calculate ratio of dark to light pixels in potential text areas
    dark_ratio = np.mean(dark_pixels == 0)
    
    # Higher dark ratio might indicate bold text
    return dark_ratio > 0.1

