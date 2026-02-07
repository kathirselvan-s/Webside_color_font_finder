# 🎨 Website Color Theme Analyzer

A powerful **AI-powered web application** that extracts and analyzes color palettes and typography from website screenshots. Perfect for designers, developers, and UI/UX professionals who want to quickly identify and understand color schemes and font styles.

---

## ✨ Features

### 🎯 **Color Analysis**
- **Intelligent Color Extraction**: Uses advanced KMeans clustering to identify dominant colors from screenshots
- **Primary, Secondary & Accent Colors**: Automatically classifies colors by role and importance
- **Complete Palette**: Extracts up to 5 unique colors with percentages and RGB values
- **Color Naming**: Automatically names each color based on CSS3 color standards
- **Contrast Analysis**: Calculates text color recommendations for optimal readability
- **Multiple Formats**: Get colors in HEX, RGB, and descriptive color names

### 🔤 **Typography Analysis**
- **Font Detection**: Analyzes image to detect font styles (serif, sans-serif, monospace)
- **Size Estimation**: Estimates heading, body, and small text sizes
- **Font Recommendations**: Suggests professional font stacks for your design
- **Text Sample Preview**: See how recommended fonts look with your detected sizes

### 📸 **User-Friendly Interface**
- **Drag & Drop Upload**: Simply drag your screenshot or click to browse
- **Live Preview**: See your uploaded image before analysis
- **One-Click Copy**: Easily copy any color code to your clipboard
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile
- **Beautiful UI**: Modern gradient design with smooth animations and hover effects

---

## 🚀 Getting Started

### Prerequisites

Make sure you have **Python 3.7+** installed on your system.

### Installation

1. **Clone or Download the Project**
   ```bash
   cd website-color-theme-analyzer
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Tesseract (Optional but Recommended for Better Font Detection)**
   
   **Windows:**
   - Download from: https://github.com/UB-Mannheim/tesseract/wiki
   - Run the installer
   - Add to PATH or update the path in your code

   **macOS:**
   ```bash
   brew install tesseract
   ```

   **Linux:**
   ```bash
   sudo apt-get install tesseract-ocr
   ```

4. **Run the Application**
   ```bash
   python app.py
   ```

5. **Open in Browser**
   ```
   http://localhost:5000
   ```

---

## 📋 Requirements

All dependencies are listed in `requirements.txt`:

- **Flask** ≥ 2.0 - Web framework for the application
- **Pillow** ≥ 9.0 - Image processing and manipulation
- **NumPy** ≥ 1.21 - Numerical computing for color analysis
- **Scikit-learn** ≥ 1.0 - Machine learning for KMeans clustering
- **WebColors** ≥ 1.11 - CSS3 color name mapping
- **Pytesseract** ≥ 0.3.10 - OCR for font/text detection

---

## 📁 Project Structure

```
website-color-theme-analyzer/
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── static/
│   ├── css/
│   │   └── style.css               # Beautiful styling and animations
│   └── js/
│       └── main.js                 # Frontend interactivity (drag-drop, copy)
├── templates/
│   ├── index.html                  # Upload page UI
│   └── result.html                 # Analysis results display
├── utils/
│   ├── color_utils.py              # Core color analysis algorithms
│   └── font_utils.py               # Font detection and analysis
└── uploads/                        # Folder for uploaded images
```

---

## 💻 How to Use

### Step 1: Upload Your Screenshot
- Navigate to the web application (http://localhost:5000)
- **Drag and drop** a website screenshot, OR
- **Click "Browse Files"** to select an image
- Supported formats: PNG, JPG, JPEG, WEBP (max 16MB)

### Step 2: Preview & Analyze
- Review the image preview
- Click **"✨ Analyze Colors"** button
- Wait for the analysis to complete (usually 2-5 seconds)

### Step 3: View Results
The analysis page displays:

#### 🎯 **Theme Colors**
- **Primary Color**: Main brand/accent color
- **Secondary Color**: Supporting color
- **Accent Color**: Highlighting or emphasis color
- **Background Color**: Main background of the website

Each color shows:
- Color swatch (clickable to copy)
- HEX code
- RGB values
- Color name
- Percentage of dominance in the image

#### 🎨 **Complete Color Palette**
- All 5 extracted colors in a grid
- Easy comparison and selection
- Click any swatch to copy the HEX code

#### 📝 **Text & Contrast**
- Recommended text color for readability
- Preview on the detected background color
- Contrast ratio information

#### 🔤 **Typography Insights**
- Detected font style
- Estimated heading, body, and small text sizes
- Preview of recommended fonts
- Professional font stack recommendations

### Tip: Quick Copy
Simply **click on any color swatch** to copy its HEX code to your clipboard!

---

## 🔧 Technical Details

### Color Analysis Algorithm
1. **Image Resizing**: Reduces large images for faster processing (max 800px)
2. **Pixel Sampling**: Takes up to 100,000 random pixels for analysis
3. **KMeans Clustering**: Groups similar colors into 5 dominant clusters
4. **Color Mapping**: Matches RGB values to nearest CSS3 color names
5. **Sorting**: Organizes colors by significance and role

### Font Detection Algorithm
1. **Edge Detection**: Analyzes image edges to detect font characteristics
2. **OCR Analysis** (if Tesseract available): Extracts text and estimates font sizes
3. **Style Classification**: Determines serif/sans-serif/monospace
4. **Boldness Detection**: Identifies if bold text is used
5. **Recommendations**: Suggests appropriate font stacks

### Color Contrast Calculation
- Uses WCAG luminance formula
- Calculates contrast ratios for readability
- Recommends optimal text colors for accessibility

---

## 🎯 Use Cases

✅ **Web Designers** - Analyze competitor websites and extract their color schemes

✅ **UI/UX Developers** - Create design systems based on existing color palettes

✅ **Brand Teams** - Ensure color consistency across digital products

✅ **Students** - Learn about color theory and design principles

✅ **Content Creators** - Build visually consistent brand identities

✅ **Marketers** - Understand the psychology of competitor branding

---

## 🐛 Troubleshooting

**Problem: "Pytesseract not found" error**
- Solution: Install Tesseract using the instructions above

**Problem: Image upload fails**
- Solution: Ensure image is less than 16MB and in supported format

**Problem: Color analysis seems inaccurate**
- Solution: Try a larger or clearer screenshot with distinct colors

**Problem: Font detection not working**
- Solution: Install Tesseract-OCR for improved detection

---

## 🔐 Security Features

- ✅ Secure file upload with extension validation
- ✅ Maximum file size limit (16MB)
- ✅ Unique filename generation
- ✅ Uploaded files stored in isolated folder
- ✅ No external data transmission

---

## 📊 Performance

- **Fast Analysis**: Most images processed in 2-5 seconds
- **Optimized Processing**: Smart image resizing to balance quality and speed
- **Efficient Clustering**: MiniBatchKMeans for large image datasets
- **Responsive UI**: Smooth animations and instant feedback

---

## 🎓 Learning Resources

- **Color Theory**: Understanding primary, secondary, and accent colors
- **Web Design**: Building cohesive color schemes
- **UX Best Practices**: Contrast ratios and accessibility
- **Font Pairing**: Choosing complementary typography

---

## 📝 API Structure

### Backend Routes

**POST `/`**
- Upload screenshot
- Returns: Analysis results page with color and font data

**GET `/uploads/<filename>`**
- Serve uploaded image file
- Used for displaying the analyzed screenshot

---

## 🎨 Customization

### Change Upload Folder Size Limit
In `app.py`:
```python
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Change 16 to desired MB
```

### Adjust Number of Colors Extracted
In `app.py` (in the analyze_image_colors call):
```python
color_result = analyze_image_colors(path, num_colors=5)  # Change 5 to desired count
```

### Customize Styling
Edit `static/css/style.css` to match your brand colors and design preferences

---

## 🤝 Contributing

Have ideas for improvements? Your feedback is valuable!

### Share Feature Ideas
- Suggest new color extraction algorithms
- Request better font detection
- Propose UI/UX improvements
- Report bugs and issues

---

## 💌 Contact & Support

**Have ideas for the next version?**

We'd love to hear from you! Share your suggestions, feature requests, or feedback:

📧 **Email:** skathirselvan12@gmail.com

Please include:
- Your feature idea or suggestion
- Your use case
- Any mockups or examples if applicable

---

## 📄 License

This project is open-source and available for personal and commercial use.

---

## ⭐ Show Your Support

If you find this tool helpful:
- ⭐ Star this repository
- 📢 Share with fellow designers and developers
- 💬 Send feedback to skathirselvan12@gmail.com

---

## 🚀 Version History

### v1.0 (Current)
- ✨ Website color analysis with KMeans clustering
- 🔤 Font style and size detection
- 📸 Drag & drop file upload
- 🎨 Beautiful modern UI with animations
- 📋 Complete color palette export

### Future Plans
- 🎯 Color harmony suggestions
- 🖼️ Multiple screenshot analysis
- 💾 Export color palette as JSON/CSS/SCSS
- 🌙 Dark mode support
- 📱 Mobile screenshot analysis
- 🔗 URL-based screenshot capture

---

## 🙏 Thank You

Thank you for using Website Color Theme Analyzer! 

**Questions? Suggestions? Ideas?**

📧 Contact: skathirselvan12@gmail.com

Happy designing! 🎨✨

---

<div align="center">

**Made with ❤️ for designers and developers**

*Extract. Analyze. Create.*

</div>
