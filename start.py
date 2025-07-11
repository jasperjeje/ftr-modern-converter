#!/usr/bin/env python3
"""
现代文件转换器 - 启动入口
左右分栏：左侧启动选择器，右侧更新日志时间线
"""

import sys
import os
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class StartupInterface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🚀 现代文件转换器 - 启动中心")
        self.root.geometry("1000x700")
        self.root.minsize(900, 600)
        
        # 设置窗口居中
        self.center_window()
        
        # 颜色主题
        self.colors = {
            'primary': '#2563eb',
            'primary_dark': '#1d4ed8',
            'secondary': '#10b981',
            'warning': '#f59e0b',
            'danger': '#ef4444',
            'light': '#f8fafc',
            'dark': '#1e293b',
            'muted': '#64748b',
            'white': '#ffffff',
            'border': '#e2e8f0'
        }
        
        self.setup_ui()
        
    def center_window(self):
        """窗口居中"""
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (1000 // 2)
        y = (self.root.winfo_screenheight() // 2) - (700 // 2)
        self.root.geometry(f"1000x700+{x}+{y}")
        
    def setup_ui(self):
        """设置界面"""
        # 主容器
        main_container = tk.Frame(self.root, bg=self.colors['light'])
        main_container.pack(fill='both', expand=True)
        
        # 头部区域
        self.create_header(main_container)
        
        # 内容区域 - 左右分栏
        content_frame = tk.Frame(main_container, bg=self.colors['light'])
        content_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # 左侧启动选择器
        left_frame = tk.Frame(content_frame, bg=self.colors['white'], relief='solid', borderwidth=1)
        left_frame.pack(side='left', fill='both', expand=True, padx=(0, 10))
        
        # 右侧更新日志时间线
        right_frame = tk.Frame(content_frame, bg=self.colors['white'], relief='solid', borderwidth=1)
        right_frame.pack(side='right', fill='both', expand=True, padx=(10, 0))
        
        # 设置内容
        self.setup_launcher_panel(left_frame)
        self.setup_changelog_panel(right_frame)
        
        # 底部状态栏
        self.create_footer(main_container)
        
    def create_header(self, parent):
        """创建头部"""
        header = tk.Frame(parent, bg=self.colors['primary'], height=80)
        header.pack(fill='x')
        header.pack_propagate(False)
        
        # 标题容器
        title_frame = tk.Frame(header, bg=self.colors['primary'])
        title_frame.pack(expand=True, fill='both')
        
        # 主标题
        title_label = tk.Label(title_frame,
                              text="🚀 现代文件转换器 - 启动中心",
                              font=('Helvetica', 20, 'bold'),
                              fg=self.colors['white'],
                              bg=self.colors['primary'])
        title_label.pack(pady=(15, 5))
        
        # 副标题
        subtitle_label = tk.Label(title_frame,
                                 text="选择启动方式 | 查看最新更新",
                                 font=('Helvetica', 11),
                                 fg=self.colors['light'],
                                 bg=self.colors['primary'])
        subtitle_label.pack(pady=(0, 15))
        
    def setup_launcher_panel(self, parent):
        """设置左侧启动面板"""
        # 内边距容器
        container = tk.Frame(parent, bg=self.colors['white'])
        container.pack(fill='both', expand=True, padx=25, pady=25)
        
        # 面板标题
        title_label = tk.Label(container,
                              text="🎯 选择启动方式",
                              font=('Helvetica', 16, 'bold'),
                              fg=self.colors['dark'],
                              bg=self.colors['white'])
        title_label.pack(pady=(0, 20))
        
        # 环境检查状态
        self.status_frame = tk.Frame(container, bg=self.colors['light'], relief='solid', borderwidth=1)
        self.status_frame.pack(fill='x', pady=(0, 20))
        
        self.check_environment()
        
        # 启动选项
        options = [
            ("🎨 现代界面", "推荐选择 - 全新设计体验", self.colors['primary'], self.launch_modern),
            ("📄 经典界面", "简洁稳定 - 传统操作界面", self.colors['muted'], self.launch_classic),
            ("⌨️ 命令行模式", "高级用户 - CLI命令操作", self.colors['warning'], self.launch_cli),
            ("🎛️ 界面选择器", "选择界面 - 详细功能介绍", self.colors['secondary'], self.launch_selector)
        ]
        
        for title, desc, color, command in options:
            self.create_launch_option(container, title, desc, color, command)
            
    def create_launch_option(self, parent, title, description, color, command):
        """创建启动选项"""
        option_frame = tk.Frame(parent, bg=self.colors['white'], relief='solid', borderwidth=1)
        option_frame.pack(fill='x', pady=(0, 12))
        
        # 启动按钮
        btn = tk.Button(option_frame,
                       text=title,
                       command=command,
                       font=('Helvetica', 12, 'bold'),
                       bg=color,
                       fg=self.colors['white'],
                       activebackground=color,
                       activeforeground=self.colors['white'],
                       relief='flat',
                       padx=20,
                       pady=12,
                       cursor='hand2')
        btn.pack(fill='x', padx=15, pady=(15, 5))
        
        # 描述文字
        desc_label = tk.Label(option_frame,
                             text=description,
                             font=('Helvetica', 10),
                             fg=self.colors['muted'],
                             bg=self.colors['white'])
        desc_label.pack(pady=(0, 15))
        
    def setup_changelog_panel(self, parent):
        """设置右侧更新日志面板"""
        # 内边距容器
        container = tk.Frame(parent, bg=self.colors['white'])
        container.pack(fill='both', expand=True, padx=25, pady=25)
        
        # 面板标题
        title_label = tk.Label(container,
                              text="📝 更新日志时间线",
                              font=('Helvetica', 16, 'bold'),
                              fg=self.colors['dark'],
                              bg=self.colors['white'])
        title_label.pack(pady=(0, 20))
        
        # 滚动区域
        scroll_frame = tk.Frame(container, bg=self.colors['white'])
        scroll_frame.pack(fill='both', expand=True)
        
        # 滚动条
        scrollbar = tk.Scrollbar(scroll_frame)
        scrollbar.pack(side='right', fill='y')
        
        # 画布
        canvas = tk.Canvas(scroll_frame,
                          bg=self.colors['white'],
                          yscrollcommand=scrollbar.set,
                          highlightthickness=0)
        canvas.pack(side='left', fill='both', expand=True)
        scrollbar.config(command=canvas.yview)
        
        # 内容框架
        content_frame = tk.Frame(canvas, bg=self.colors['white'])
        canvas.create_window((0, 0), window=content_frame, anchor='nw')
        
        # 添加更新日志条目
        self.add_changelog_items(content_frame)
        
        # 更新滚动区域
        content_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox('all'))
        
        # 绑定鼠标滚轮
        def on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        canvas.bind('<MouseWheel>', on_mousewheel)
        
    def add_changelog_items(self, parent):
        """添加更新日志条目"""
        updates = [
            {
                "version": "v2.2",
                "date": "2025-01-11",
                "title": "启动器界面优化",
                "changes": [
                    "✨ 根据源文件智能显示可用的目标格式",
                    "🎨 Windows使用UTF - 8 - sig，macOS使用UTF - 8",
                    "🔧 现代界面从1200x800增加到1200x900",
                    "📋 不支持的格式自动禁用，防止无效转换"
                ],
                "color": "#10b981"
            },
            {
                "version": "v2.1",
                "date": "2025-01-11",
                "title": "启动器界面优化",
                "changes": [
                    "✨ 新增启动中心，集成所有启动方式",
                    "🎨 左右分栏布局，展示更新日志时间线",
                    "🔧 优化界面选择器，窗口扩大到550x650",
                    "📋 添加详细功能介绍和使用指导"
                ],
                "color": "#10b981"
            },
            {
                "version": "v2.0",
                "date": "2025-01-11",
                "title": "PDF转Markdown + 现代界面",
                "changes": [
                    "📄 新增PDF转Markdown功能，智能识别文档结构",
                    "🎨 全新现代化界面设计，提升用户体验",
                    "🔄 修复界面显示问题，优化窗口大小",
                    "🎯 改进按钮颜色对比度，格式选择更清晰"
                ],
                "color": "#2563eb"
            },
            {
                "version": "v1.5",
                "date": "2025-01-10",
                "title": "界面布局优化",
                "changes": [
                    "📐 窗口大小从1000x700增加到1200x800",
                    "🎨 格式按钮从4列改为3列布局",
                    "🔤 日志字体改为Courier New提升兼容性",
                    "⚡ 优化进度条样式和显示效果"
                ],
                "color": "#f59e0b"
            },
            {
                "version": "v1.0",
                "date": "2025-01-09",
                "title": "基础功能版本",
                "changes": [
                    "🚀 项目初始化，核心转换功能",
                    "📄 支持PDF与DOCX互转",
                    "🖼️ 支持多种图像格式转换",
                    "📊 支持CSV与XLSX表格转换"
                ],
                "color": "#64748b"
            }
        ]
        
        for i, update in enumerate(updates):
            self.create_changelog_item(parent, update, i == 0)
            
    def create_changelog_item(self, parent, update, is_latest=False):
        """创建更新日志条目"""
        # 主容器
        item_frame = tk.Frame(parent, bg=self.colors['white'])
        item_frame.pack(fill='x', pady=(0, 20))
        
        # 左侧时间线
        timeline_frame = tk.Frame(item_frame, bg=self.colors['white'], width=60)
        timeline_frame.pack(side='left', fill='y')
        timeline_frame.pack_propagate(False)
        
        # 时间线圆点
        dot_color = update['color'] if is_latest else self.colors['muted']
        dot_frame = tk.Frame(timeline_frame, bg=dot_color, width=12, height=12)
        dot_frame.pack(pady=(15, 0))
        dot_frame.pack_propagate(False)
        
        # 时间线连接线（除了最后一个）
        line_frame = tk.Frame(timeline_frame, bg=self.colors['border'], width=2)
        line_frame.pack(fill='y', expand=True, pady=(5, 0))
        
        # 右侧内容
        content_frame = tk.Frame(item_frame, bg=self.colors['light'], relief='solid', borderwidth=1)
        content_frame.pack(side='right', fill='both', expand=True, padx=(10, 0))
        
        # 版本和日期
        header_frame = tk.Frame(content_frame, bg=update['color'] if is_latest else self.colors['muted'])
        header_frame.pack(fill='x')
        
        version_label = tk.Label(header_frame,
                                text=f"{update['version']} - {update['title']}",
                                font=('Helvetica', 12, 'bold'),
                                fg=self.colors['white'],
                                bg=update['color'] if is_latest else self.colors['muted'])
        version_label.pack(side='left', padx=15, pady=8)
        
        date_label = tk.Label(header_frame,
                             text=update['date'],
                             font=('Helvetica', 10),
                             fg=self.colors['light'],
                             bg=update['color'] if is_latest else self.colors['muted'])
        date_label.pack(side='right', padx=15, pady=8)
        
        # 更新内容
        changes_frame = tk.Frame(content_frame, bg=self.colors['white'])
        changes_frame.pack(fill='both', expand=True, padx=15, pady=15)
        
        for change in update['changes']:
            change_label = tk.Label(changes_frame,
                                   text=change,
                                   font=('Helvetica', 10),
                                   fg=self.colors['dark'],
                                   bg=self.colors['white'],
                                   anchor='w',
                                   justify='left')
            change_label.pack(fill='x', pady=2)
            
    def check_environment(self):
        """检查环境状态"""
        status_container = tk.Frame(self.status_frame, bg=self.colors['light'])
        status_container.pack(fill='x', padx=15, pady=10)
        
        # 检查虚拟环境
        venv_status = "✅" if os.path.exists("venv") else "❌"
        venv_text = "虚拟环境已就绪" if os.path.exists("venv") else "需要安装虚拟环境"
        
        venv_label = tk.Label(status_container,
                             text=f"{venv_status} {venv_text}",
                             font=('Helvetica', 10),
                             fg=self.colors['dark'],
                             bg=self.colors['light'])
        venv_label.pack(anchor='w')
        
        # 检查依赖
        try:
            import tkinter
            from PIL import Image
            import pandas as pd
            deps_status = "✅ 依赖包已安装"
            deps_color = self.colors['dark']
        except ImportError:
            deps_status = "❌ 需要安装依赖包"
            deps_color = self.colors['danger']
            
        deps_label = tk.Label(status_container,
                             text=deps_status,
                             font=('Helvetica', 10),
                             fg=deps_color,
                             bg=self.colors['light'])
        deps_label.pack(anchor='w')
        
    def create_footer(self, parent):
        """创建底部状态栏"""
        footer = tk.Frame(parent, bg=self.colors['border'], height=40)
        footer.pack(fill='x', side='bottom')
        footer.pack_propagate(False)
        
        # 版本信息
        version_label = tk.Label(footer,
                                text="现代文件转换器 v2.1 | 支持PDF↔DOCX↔Markdown",
                                font=('Helvetica', 10),
                                fg=self.colors['dark'],
                                bg=self.colors['border'])
        version_label.pack(side='left', padx=20, pady=10)
        
        # 时间
        time_label = tk.Label(footer,
                             text=datetime.now().strftime("%Y-%m-%d %H:%M"),
                             font=('Helvetica', 10),
                             fg=self.colors['muted'],
                             bg=self.colors['border'])
        time_label.pack(side='right', padx=20, pady=10)
        
    def launch_modern(self):
        """启动现代界面"""
        self.launch_app('modern_ui', '现代界面')
        
    def launch_classic(self):
        """启动经典界面"""
        self.launch_app('main', '经典界面')
        
    def launch_cli(self):
        """启动命令行版本"""
        import subprocess
        import sys
        try:
            subprocess.run([sys.executable, "cli.py", "--help"])
        except Exception as e:
            messagebox.showerror("错误", f"无法启动命令行版本: {e}")
            
    def launch_selector(self):
        """启动界面选择器"""
        self.root.destroy()
        try:
            from launcher import show_ui_selector
            show_ui_selector()
        except Exception as e:
            messagebox.showerror("错误", f"无法启动界面选择器: {e}")
            
    def launch_app(self, module_name, app_name):
        """启动应用"""
        self.root.destroy()
        try:
            if module_name == 'modern_ui':
                from modern_ui import main as app_main
            else:
                from main import main as app_main
            app_main()
        except ImportError as e:
            messagebox.showerror("错误", f"无法启动{app_name}: {e}")
        except Exception as e:
            messagebox.showerror("错误", f"启动{app_name}时发生错误: {e}")
            
    def run(self):
        """运行界面"""
        self.root.mainloop()

def main():
    """主启动函数"""
    print("🚀 现代文件转换器 - 启动中心")
    print("=" * 50)
    
    app = StartupInterface()
    app.run()

if __name__ == "__main__":
    main()