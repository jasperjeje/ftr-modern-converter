@echo off
echo 正在为Windows打包应用程序...

REM 检查是否安装了pyinstaller
pyinstaller --version >nul 2>&1
if %errorlevel% neq 0 (
    echo PyInstaller未安装，正在安装...
    pip install pyinstaller
)

REM 清理之前的构建
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist

REM 使用spec文件打包
pyinstaller file_converter.spec

REM 检查是否成功
if exist "dist\FileConverter.exe" (
    echo ✅ Windows应用程序打包成功！
    echo 可执行文件位置: dist\FileConverter.exe
) else (
    echo ❌ 打包失败，请检查错误信息
)

pause