#!/bin/bash

# macOS打包脚本
echo "正在为macOS打包应用程序..."

# 检查是否安装了pyinstaller
if ! command -v pyinstaller &> /dev/null; then
    echo "PyInstaller未安装，正在安装..."
    pip install pyinstaller
fi

# 清理之前的构建
rm -rf build/ dist/

# 使用spec文件打包
pyinstaller file_converter.spec

# 检查是否成功
if [ -f "dist/FileConverter" ]; then
    echo "✅ macOS应用程序打包成功！"
    echo "可执行文件位置: dist/FileConverter"
    
    # 创建应用程序包
    mkdir -p "dist/FileConverter.app/Contents/MacOS"
    mkdir -p "dist/FileConverter.app/Contents/Resources"
    
    # 移动可执行文件
    mv "dist/FileConverter" "dist/FileConverter.app/Contents/MacOS/"
    
    # 创建Info.plist
    cat > "dist/FileConverter.app/Contents/Info.plist" << EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleExecutable</key>
    <string>FileConverter</string>
    <key>CFBundleIdentifier</key>
    <string>com.fileconverter.app</string>
    <key>CFBundleName</key>
    <string>FileConverter</string>
    <key>CFBundleVersion</key>
    <string>1.0</string>
    <key>CFBundlePackageType</key>
    <string>APPL</string>
    <key>CFBundleSignature</key>
    <string>????</string>
</dict>
</plist>
EOF
    
    echo "✅ 应用程序包创建成功: dist/FileConverter.app"
else
    echo "❌ 打包失败，请检查错误信息"
fi