#!/bin/bash

# 现代文件转换器 - macOS打包工具
echo "========================================"
echo "   现代文件转换器 - macOS打包工具"
echo "========================================"
echo

# 检查Python是否安装
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3未安装"
    echo "请安装Python 3.7+："
    echo "  brew install python3"
    echo "  或从 https://python.org 下载"
    exit 1
fi

# 显示Python版本
echo "🐍 Python版本: $(python3 --version)"

# 激活虚拟环境（如果存在）
if [ -f "venv/bin/activate" ]; then
    echo "🔄 激活虚拟环境..."
    source venv/bin/activate
fi

# 运行跨平台构建脚本
echo "🚀 开始构建macOS应用程序..."
python3 build_cross_platform.py

# 检查构建结果
if [ -d "release/ModernFileConverter_v2.2.0_macOS" ]; then
    echo
    echo "✅ macOS应用程序构建成功！"
    echo "📦 应用程序位置: release/ModernFileConverter_v2.2.0_macOS/"
    echo
    echo "🎯 下一步："
    echo "  1. 复制ModernFileConverter.app到应用程序文件夹"
    echo "  2. 双击运行或从Launchpad启动"
    echo
    
    # 尝试打开发布目录
    if command -v open &> /dev/null; then
        echo "📂 正在打开发布目录..."
        open release/
    fi
else
    echo
    echo "❌ 构建失败，请检查错误信息"
    echo
fi

echo "按任意键继续..."
read -n 1