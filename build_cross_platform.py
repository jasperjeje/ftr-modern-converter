#!/usr/bin/env python3
"""
跨平台打包脚本
支持在Windows和macOS环境下打包应用程序
"""

import os
import sys
import platform
import subprocess
import shutil
from datetime import datetime

class CrossPlatformBuilder:
    def __init__(self):
        self.system = platform.system()
        self.python_exe = sys.executable
        self.project_dir = os.path.dirname(os.path.abspath(__file__))
        
        # 应用信息
        self.app_name = "ModernFileConverter"
        self.app_version = "2.2.0"
        self.app_display_name = "现代文件转换器"
        
    def print_header(self):
        """打印头部信息"""
        print("=" * 60)
        print(f"🚀 {self.app_display_name} - 跨平台打包工具")
        print("=" * 60)
        print(f"📅 打包时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"🖥️  操作系统: {self.system}")
        print(f"🐍 Python版本: {platform.python_version()}")
        print(f"📁 项目目录: {self.project_dir}")
        print("=" * 60)
        
    def check_dependencies(self):
        """检查依赖"""
        print("🔍 检查依赖...")
        
        # 检查PyInstaller
        try:
            result = subprocess.run([self.python_exe, '-m', 'pyinstaller', '--version'], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                version = result.stdout.strip()
                print(f"  ✅ PyInstaller {version}")
            else:
                raise subprocess.CalledProcessError(result.returncode, 'pyinstaller')
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("  ❌ PyInstaller未安装，正在安装...")
            subprocess.run([self.python_exe, '-m', 'pip', 'install', '--break-system-packages', 'pyinstaller'])
            print("  ✅ PyInstaller安装完成")
        
        # 读取并安装requirements.txt中的依赖
        requirements_file = os.path.join(self.project_dir, 'requirements.txt')
        if os.path.exists(requirements_file):
            print("  📦 安装项目依赖...")
            result = subprocess.run([
                self.python_exe, '-m', 'pip', 'install', 
                '--break-system-packages', '-r', requirements_file
            ], capture_output=True, text=True)
            
            if result.returncode == 0:
                print("  ✅ 项目依赖安装完成")
            else:
                print(f"  ⚠️  部分依赖安装失败: {result.stderr}")
        
        # 检查核心模块
        core_modules = ['tkinter']
        for module in core_modules:
            try:
                __import__(module)
                print(f"  ✅ {module}")
            except ImportError:
                print(f"  ❌ {module} 未安装")
                return False
        
        # 检查可选模块
        optional_modules = [
            'PIL', 'pandas', 'openpyxl', 
            'docx', 'PyPDF2', 'reportlab'
        ]
        
        missing_optional = []
        for module in optional_modules:
            try:
                __import__(module)
                print(f"  ✅ {module}")
            except ImportError:
                missing_optional.append(module)
                print(f"  ⚠️  {module} 未安装 (功能可能受限)")
        
        if missing_optional:
            print(f"  💡 缺少可选模块: {', '.join(missing_optional)}")
            print("  📄 应用程序仍可打包，但某些功能可能不可用")
        
        return True
        
    def clean_build(self):
        """清理构建目录"""
        print("🧹 清理构建目录...")
        
        dirs_to_clean = ['build', 'dist', '__pycache__']
        for dir_name in dirs_to_clean:
            dir_path = os.path.join(self.project_dir, dir_name)
            if os.path.exists(dir_path):
                shutil.rmtree(dir_path)
                print(f"  🗑️  删除: {dir_name}")
        
        # 清理.pyc文件
        for root, dirs, files in os.walk(self.project_dir):
            for file in files:
                if file.endswith('.pyc'):
                    os.remove(os.path.join(root, file))
                    
    def build_application(self):
        """构建应用程序"""
        print(f"🔨 开始构建 {self.system} 应用程序...")
        
        spec_file = os.path.join(self.project_dir, 'modern_converter.spec')
        
        # 执行PyInstaller
        cmd = ['pyinstaller', spec_file, '--clean']
        
        print(f"📋 执行命令: {' '.join(cmd)}")
        result = subprocess.run(cmd, cwd=self.project_dir)
        
        if result.returncode != 0:
            print("❌ 构建失败")
            return False
            
        return True
        
    def verify_build(self):
        """验证构建结果"""
        print("🔍 验证构建结果...")
        
        if self.system == 'Windows':
            exe_path = os.path.join(self.project_dir, 'dist', f'{self.app_name}.exe')
            if os.path.exists(exe_path):
                size = os.path.getsize(exe_path) / (1024 * 1024)
                print(f"  ✅ Windows可执行文件: {exe_path}")
                print(f"  📏 文件大小: {size:.1f} MB")
                return exe_path
        elif self.system == 'Darwin':
            app_path = os.path.join(self.project_dir, 'dist', f'{self.app_name}.app')
            exe_path = os.path.join(app_path, 'Contents', 'MacOS', self.app_name)
            if os.path.exists(app_path) and os.path.exists(exe_path):
                # 计算应用包大小
                total_size = 0
                for root, dirs, files in os.walk(app_path):
                    for file in files:
                        total_size += os.path.getsize(os.path.join(root, file))
                size = total_size / (1024 * 1024)
                print(f"  ✅ macOS应用程序包: {app_path}")
                print(f"  📏 应用包大小: {size:.1f} MB")
                return app_path
        else:
            exe_path = os.path.join(self.project_dir, 'dist', self.app_name)
            if os.path.exists(exe_path):
                size = os.path.getsize(exe_path) / (1024 * 1024)
                print(f"  ✅ Linux可执行文件: {exe_path}")
                print(f"  📏 文件大小: {size:.1f} MB")
                return exe_path
                
        print("  ❌ 构建文件未找到")
        return None
        
    def create_distribution_package(self, build_path):
        """创建分发包"""
        print("📦 创建分发包...")
        
        # 创建分发目录
        dist_dir = os.path.join(self.project_dir, 'release')
        if os.path.exists(dist_dir):
            shutil.rmtree(dist_dir)
        os.makedirs(dist_dir)
        
        # 根据平台创建不同的分发包
        if self.system == 'Windows':
            # Windows: 创建ZIP包
            package_name = f"{self.app_name}_v{self.app_version}_Windows.zip"
            package_path = os.path.join(dist_dir, package_name)
            
            import zipfile
            with zipfile.ZipFile(package_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                zipf.write(build_path, f"{self.app_name}.exe")
                # 添加说明文件
                readme_content = self.create_readme_content()
                zipf.writestr("README.txt", readme_content)
                
        elif self.system == 'Darwin':
            # macOS: 创建DMG镜像（简化版，直接复制.app）
            package_name = f"{self.app_name}_v{self.app_version}_macOS"
            package_path = os.path.join(dist_dir, package_name)
            shutil.copytree(build_path, os.path.join(package_path, f"{self.app_name}.app"))
            
            # 添加说明文件
            readme_content = self.create_readme_content()
            with open(os.path.join(package_path, "README.txt"), 'w', encoding='utf-8') as f:
                f.write(readme_content)
                
        else:
            # Linux: 创建tar.gz包
            package_name = f"{self.app_name}_v{self.app_version}_Linux.tar.gz"
            package_path = os.path.join(dist_dir, package_name)
            
            import tarfile
            with tarfile.open(package_path, 'w:gz') as tar:
                tar.add(build_path, f"{self.app_name}")
                # 添加说明文件
                readme_content = self.create_readme_content()
                import io
                readme_tarinfo = tarfile.TarInfo(name="README.txt")
                readme_tarinfo.size = len(readme_content.encode('utf-8'))
                tar.addfile(readme_tarinfo, io.BytesIO(readme_content.encode('utf-8')))
        
        print(f"  ✅ 分发包已创建: {package_path}")
        return package_path
        
    def create_readme_content(self):
        """创建README内容"""
        return f"""
Modern File Converter v{self.app_version}
=====================================================

🚀 A modern and powerful file conversion tool

## Features
✨ PDF to Markdown conversion
📄 Multiple document format support (PDF ↔ DOCX)
🖼️ Image format conversion (JPG/PNG/GIF/BMP)
📊 Spreadsheet format conversion (CSV ↔ XLSX)
🎨 Modern user interface
🌍 Cross-platform support (Windows/macOS/Linux)

## System Requirements
- {self.system} 10.14+ (macOS) / Windows 10+ / Linux
- No additional Python installation required

## Usage
1. Double-click the executable file
2. Select source file
3. Choose target format
4. Click convert

## Technical Information
- Version: {self.app_version}
- Build Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
- Platform: {self.system}

For more information, visit the project homepage.
"""
        
    def run(self):
        """运行构建流程"""
        try:
            self.print_header()
            
            # 检查依赖
            if not self.check_dependencies():
                print("❌ 依赖检查失败")
                return False
                
            # 清理构建目录
            self.clean_build()
            
            # 构建应用程序
            if not self.build_application():
                print("❌ 构建失败")
                return False
                
            # 验证构建结果
            build_path = self.verify_build()
            if not build_path:
                print("❌ 构建验证失败")
                return False
                
            # 创建分发包
            package_path = self.create_distribution_package(build_path)
            
            print("\n" + "=" * 60)
            print("🎉 构建完成！")
            print(f"📦 分发包: {package_path}")
            print("=" * 60)
            
            return True
            
        except Exception as e:
            print(f"❌ 构建过程中发生错误: {e}")
            return False

def main():
    """主函数"""
    builder = CrossPlatformBuilder()
    success = builder.run()
    
    if not success:
        print("\n❌ 构建失败，请检查错误信息")
        return 1
        
    print("\n✅ 构建成功完成！")
    return 0

if __name__ == "__main__":
    sys.exit(main())