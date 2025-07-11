@echo off
chcp 65001 >nul 2>&1
echo.
echo ========================================
echo   现代文件转换器 - Windows打包工具
echo ========================================
echo.

REM 检查Python是否安装
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python未安装或未添加到PATH
    echo 请安装Python 3.7+并添加到系统PATH
    pause
    exit /b 1
)

REM 激活虚拟环境（如果存在）
if exist "venv\Scripts\activate.bat" (
    echo 🔄 激活虚拟环境...
    call venv\Scripts\activate.bat
)

REM 运行跨平台构建脚本
echo 🚀 开始构建Windows应用程序...
python build_cross_platform.py

REM 检查构建结果
if exist "release\ModernFileConverter_v2.2.0_Windows.zip" (
    echo.
    echo ✅ Windows应用程序构建成功！
    echo 📦 分发包位置: release\ModernFileConverter_v2.2.0_Windows.zip
    echo.
    echo 🎯 下一步：
    echo   1. 解压ZIP文件
    echo   2. 双击ModernFileConverter.exe运行
    echo.
) else (
    echo.
    echo ❌ 构建失败，请检查错误信息
    echo.
)

pause