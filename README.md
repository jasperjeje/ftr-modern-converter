# Modern File Converter

> 🚀 A modern and powerful file conversion tool | 现代化的文件转换工具

[中文版本](README_zh.md) | [English Version](README.md)

<div align="center" style="display: flex; gap: 20px; justify-content: center; flex-wrap: wrap;">
  <img src="./images/image.png" alt="现代文件转换器 - 启动中心" width="48%" style="max-width: 400px; border-radius: 8px; box-shadow: 0 4px 20px rgba(0,0,0,0.1);">
  <img src="./images/image2.png" alt="现代文件转换器 - 转换界面" width="48%" style="max-width: 400px; border-radius: 8px; box-shadow: 0 4px 20px rgba(0,0,0,0.1);">
</div>

## Features

✨ **PDF to Markdown Conversion** - Convert PDF documents to Markdown format  
📄 **Document Format Support** - Convert between PDF and DOCX formats  
🖼️ **Image Format Support** - Convert between JPG, PNG, GIF, and BMP formats  
📊 **Spreadsheet Support** - Convert between CSV and XLSX formats  
🎨 **Modern UI Design** - Clean and intuitive user interface  
🌍 **Cross-Platform** - Works on Windows, macOS, and Linux  
🔄 **Dynamic Format Detection** - Automatically shows available conversion options  
🔧 **Smart Encoding** - Handles different file encodings across platforms  

## System Requirements

- **Windows**: Windows 10 or later
- **macOS**: macOS 10.14 (Mojave) or later
- **Linux**: Modern Linux distributions
- **Dependencies**: All required libraries are bundled in the executable

## Installation & Usage

### Option 1: Download Pre-built Executable

1. Download the latest release for your platform from the releases page
2. Extract the files (Windows) or copy the .app bundle (macOS)
3. Run the executable file

### Option 2: Build from Source

#### Prerequisites
- Python 3.7 or later
- pip package manager

#### Installation
```bash
# Clone the repository
git clone [repository-url]
cd ftr

# Install dependencies
pip install -r requirements.txt

# Run the application
python start.py
```

#### Building Executable

**For Windows:**
```bash
# Run the build script
build_windows_new.bat
```

**For macOS:**
```bash
# Make the script executable
chmod +x build_macos_new.sh

# Run the build script
./build_macos_new.sh
```

**Cross-Platform Build:**
```bash
# Use the universal build script
python build_cross_platform.py
```

## How to Use

1. **Launch the Application**
   - Double-click the executable file
   - Choose your preferred interface (Classic or Modern)

2. **Select Source File**
   - Click "Browse" to select your input file
   - Supported formats will be automatically detected

3. **Choose Target Format**
   - Available conversion options will be displayed
   - Select your desired output format

4. **Convert**
   - Click "Start Conversion"
   - Monitor progress in the status bar
   - Find your converted file in the same directory

## Supported Formats

### Document Conversion
- **PDF** ↔ **DOCX**: Bidirectional document conversion
- **PDF** → **Markdown**: Convert PDF to Markdown with intelligent formatting

### Image Conversion
- **JPG** ↔ **PNG** ↔ **GIF** ↔ **BMP**: Convert between image formats
- **TIFF** → **JPG/PNG**: Convert TIFF images to common formats

### Spreadsheet Conversion
- **CSV** ↔ **XLSX**: Convert between CSV and Excel formats
- **XLS** → **XLSX**: Upgrade legacy Excel files

## Features in Detail

### PDF to Markdown Conversion
- Extracts text content from PDF files
- Preserves basic formatting structure
- Handles multiple pages
- Creates clean, readable Markdown output

### Modern Interface
- Card-based layout design
- Real-time format availability
- Progress tracking
- Responsive design

### Cross-Platform Compatibility
- Native file encoding handling
- Platform-specific optimizations
- Consistent behavior across systems

## Technical Details

### Built With
- **Python 3.13** - Core application language
- **Tkinter** - GUI framework
- **PyPDF2** - PDF processing
- **Pillow** - Image processing
- **pandas** - Data manipulation
- **python-docx** - Word document handling
- **ReportLab** - PDF generation

### Architecture
- Modular design with separate UI and conversion logic
- Thread-safe file operations
- Dynamic format detection system
- Cross-platform encoding management

## Development

### Project Structure
```
ftr/
├── start.py              # Main application launcher
├── modern_ui.py          # Modern interface implementation
├── file_converter.py     # Core conversion logic
├── launcher.py           # Interface selection
├── requirements.txt      # Python dependencies
├── build_cross_platform.py  # Build script
└── README.md            # This file
```

### Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Version History

### v2.2.0 (Current)
- ✅ PDF to Markdown conversion
- ✅ Modern UI redesign
- ✅ Dynamic format detection
- ✅ Cross-platform encoding fixes
- ✅ Unified packaging system

### v2.1.0
- Added modern interface option
- Improved file format support
- Enhanced error handling

### v2.0.0
- Complete UI redesign
- Added multiple format support
- Improved conversion accuracy

## Support

If you encounter any issues or have questions:

1. Check the [FAQ section](docs/FAQ.md)
2. Review existing [issues](issues)
3. Create a new issue with detailed information

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Thanks to all contributors and testers
- Special thanks to the Python community for excellent libraries
- UI design inspired by modern application standards

---

**Modern File Converter** - Making file conversion simple and beautiful.