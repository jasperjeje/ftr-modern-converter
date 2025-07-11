#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
现代文件转换器 - 现代化界面模块

Copyright 2024 现代文件转换器项目

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import threading
from file_converter import FileConverter
from datetime import datetime

class ModernFileConverterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("现代文件转换器")
        self.root.geometry("1200x900")
        self.root.minsize(1000, 750)
        
        # 设置主题色彩
        self.colors = {
            'primary': '#2563eb',      # 蓝色
            'primary_dark': '#1d4ed8',
            'secondary': '#10b981',    # 绿色
            'danger': '#ef4444',       # 红色
            'warning': '#f59e0b',      # 黄色
            'light': '#f8fafc',        # 浅灰
            'dark': '#1e293b',         # 深灰
            'muted': '#64748b',        # 中灰
            'white': '#ffffff',
            'border': '#e2e8f0'
        }
        
        self.converter = FileConverter()
        self.setup_modern_ui()
        
        # 设置样式
        self.setup_styles()
        
    def setup_styles(self):
        """设置现代化样式"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # 配置样式
        style.configure('Title.TLabel', 
                       font=('Helvetica', 28, 'bold'),
                       foreground=self.colors['dark'])
        
        style.configure('Subtitle.TLabel', 
                       font=('Helvetica', 12),
                       foreground=self.colors['muted'])
        
        style.configure('Section.TLabel', 
                       font=('Helvetica', 14, 'bold'),
                       foreground=self.colors['dark'])
        
        style.configure('Modern.TButton',
                       font=('Helvetica', 10, 'bold'),
                       padding=(20, 10))
        
        style.configure('Primary.TButton',
                       font=('Helvetica', 12, 'bold'),
                       padding=(30, 15))
        
        style.configure('Modern.TFrame',
                       background=self.colors['white'],
                       relief='flat',
                       borderwidth=1)
        
        style.configure('Card.TFrame',
                       background=self.colors['white'],
                       relief='solid',
                       borderwidth=1)
        
    def setup_modern_ui(self):
        """设置现代化UI"""
        # 主容器
        main_container = tk.Frame(self.root, bg=self.colors['light'])
        main_container.pack(fill='both', expand=True, padx=0, pady=0)
        
        # 创建头部
        self.create_header(main_container)
        
        # 创建内容区域
        content_frame = tk.Frame(main_container, bg=self.colors['light'])
        content_frame.pack(fill='both', expand=True, padx=20, pady=15)
        
        # 左侧区域 - 文件操作
        left_frame = tk.Frame(content_frame, bg=self.colors['white'], relief='solid', borderwidth=2)
        left_frame.pack(side='left', fill='both', expand=True, padx=(0, 10))
        
        # 右侧区域 - 日志和状态
        right_frame = tk.Frame(content_frame, bg=self.colors['white'], relief='solid', borderwidth=1)
        right_frame.pack(side='right', fill='both', expand=True, padx=(10, 0))
        
        # 设置内容
        self.setup_file_operations(left_frame)
        self.setup_log_panel(right_frame)
        
        # 创建底部状态栏
        self.create_footer(main_container)
        
    def create_header(self, parent):
        """创建头部"""
        header = tk.Frame(parent, bg=self.colors['primary'], height=100)
        header.pack(fill='x', padx=0, pady=0)
        header.pack_propagate(False)
        
        # 标题和描述
        title_frame = tk.Frame(header, bg=self.colors['primary'])
        title_frame.pack(expand=True, fill='both')
        
        title_label = tk.Label(title_frame, 
                              text="🚀 现代文件转换器",
                              font=('Helvetica', 24, 'bold'),
                              fg=self.colors['white'],
                              bg=self.colors['primary'])
        title_label.pack(pady=(20, 5))
        
        subtitle_label = tk.Label(title_frame,
                                 text="支持多种格式转换，包括PDF转Markdown",
                                 font=('Helvetica', 12),
                                 fg=self.colors['light'],
                                 bg=self.colors['primary'])
        subtitle_label.pack(pady=(0, 20))
        
    def setup_file_operations(self, parent):
        """设置文件操作区域"""
        # 内边距容器
        container = tk.Frame(parent, bg=self.colors['white'])
        container.pack(fill='both', expand=True, padx=25, pady=25)
        
        # 区域标题
        title_label = tk.Label(container,
                              text="📁 文件转换",
                              font=('Helvetica', 16, 'bold'),
                              fg=self.colors['dark'],
                              bg=self.colors['white'])
        title_label.pack(anchor='w', pady=(0, 20))
        
        # 源文件选择卡片
        source_card = self.create_card(container, "选择源文件")
        
        # 源文件路径显示
        self.source_path = tk.StringVar()
        self.source_display = tk.Label(source_card,
                                      text="请选择要转换的文件",
                                      font=('Helvetica', 10),
                                      fg=self.colors['muted'],
                                      bg=self.colors['light'],
                                      relief='solid',
                                      borderwidth=1,
                                      padx=15,
                                      pady=10)
        self.source_display.pack(fill='x', pady=(0, 10))
        
        # 选择文件按钮
        browse_btn = tk.Button(source_card,
                              text="📂 浏览文件",
                              command=self.browse_source,
                              font=('Helvetica', 11, 'bold'),
                              bg=self.colors['primary'],
                              fg=self.colors['white'],
                              activebackground=self.colors['primary_dark'],
                              activeforeground=self.colors['white'],
                              relief='flat',
                              padx=25,
                              pady=12,
                              cursor='hand2')
        browse_btn.pack(pady=(0, 10))
        
        # 目标格式选择卡片
        format_card = self.create_card(container, "选择目标格式")
        
        # 格式选择按钮组
        self.target_format = tk.StringVar()
        self.format_frame = tk.Frame(format_card, bg=self.colors['white'])
        self.format_frame.pack(fill='x', pady=(0, 10))
        
        # 初始化时显示所有格式（灰色状态）
        self.all_formats = [
            ("PDF", "📄"), ("DOCX", "📝"), ("MD", "📋"),
            ("JPG", "🖼️"), ("PNG", "🖼️"), ("CSV", "📊"), ("XLSX", "📈")
        ]
        
        self.format_buttons = {}
        self.create_format_buttons()
        
        # 配置网格权重
        for i in range(3):
            self.format_frame.columnconfigure(i, weight=1)
        
        # 输出路径卡片
        output_card = self.create_card(container, "输出路径")
        
        # 输出路径显示
        self.output_path = tk.StringVar()
        self.output_display = tk.Label(output_card,
                                      text="将自动生成输出路径",
                                      font=('Helvetica', 10),
                                      fg=self.colors['muted'],
                                      bg=self.colors['light'],
                                      relief='solid',
                                      borderwidth=1,
                                      padx=15,
                                      pady=10)
        self.output_display.pack(fill='x', pady=(0, 10))
        
        # 输出路径按钮
        output_btn = tk.Button(output_card,
                              text="📁 选择输出位置",
                              command=self.browse_output,
                              font=('Helvetica', 11, 'bold'),
                              bg=self.colors['warning'],
                              fg=self.colors['white'],
                              activebackground='#d97706',
                              activeforeground=self.colors['white'],
                              relief='flat',
                              padx=25,
                              pady=12,
                              cursor='hand2')
        output_btn.pack(pady=(0, 10))
        
        # 转换按钮
        self.convert_btn = tk.Button(container,
                                    text="🚀 开始转换",
                                    command=self.start_conversion,
                                    font=('Helvetica', 14, 'bold'),
                                    bg=self.colors['secondary'],
                                    fg=self.colors['white'],
                                    activebackground='#059669',
                                    activeforeground=self.colors['white'],
                                    relief='flat',
                                    padx=40,
                                    pady=15,
                                    cursor='hand2')
        self.convert_btn.pack(pady=30)
        
        # 进度条
        self.progress = ttk.Progressbar(container, 
                                       mode='indeterminate',
                                       style='Modern.Horizontal.TProgressbar')
        self.progress.pack(fill='x', pady=(0, 20))
        
        # 配置进度条样式
        style = ttk.Style()
        style.configure('Modern.Horizontal.TProgressbar',
                       background=self.colors['secondary'],
                       troughcolor=self.colors['light'],
                       borderwidth=0,
                       lightcolor=self.colors['secondary'],
                       darkcolor=self.colors['secondary'])
        
    def create_card(self, parent, title):
        """创建卡片容器"""
        card = tk.Frame(parent, bg=self.colors['white'], relief='solid', borderwidth=1)
        card.pack(fill='x', pady=(0, 15))
        
        # 卡片标题
        title_label = tk.Label(card,
                              text=title,
                              font=('Helvetica', 12, 'bold'),
                              fg=self.colors['dark'],
                              bg=self.colors['white'])
        title_label.pack(anchor='w', pady=(10, 8))
        
        return card
        
    def create_format_buttons(self):
        """创建格式按钮"""
        # 清除现有按钮
        for widget in self.format_frame.winfo_children():
            widget.destroy()
        self.format_buttons.clear()
        
        for i, (fmt, icon) in enumerate(self.all_formats):
            btn = tk.Button(self.format_frame,
                           text=f"{icon} {fmt}",
                           command=lambda f=fmt: self.select_format(f),
                           font=('Helvetica', 10, 'bold'),
                           bg=self.colors['border'],  # 默认灰色（不可用）
                           fg=self.colors['muted'],
                           activebackground=self.colors['secondary'],
                           activeforeground=self.colors['white'],
                           relief='solid',
                           borderwidth=2,
                           padx=12,
                           pady=8,
                           cursor='hand2',
                           state='disabled')  # 默认禁用
            btn.grid(row=i//3, column=i%3, padx=8, pady=8, sticky='ew')
            self.format_buttons[fmt] = btn
            
    def update_format_buttons(self, source_path):
        """根据源文件更新格式按钮状态"""
        if not source_path:
            # 如果没有源文件，所有按钮都禁用
            for fmt, btn in self.format_buttons.items():
                btn.config(
                    bg=self.colors['border'],
                    fg=self.colors['muted'],
                    state='disabled'
                )
            return
            
        # 获取支持的目标格式
        supported_formats = self.converter.get_supported_target_formats(source_path)
        
        for fmt, btn in self.format_buttons.items():
            if fmt in supported_formats:
                # 启用支持的格式
                btn.config(
                    bg=self.colors['white'],
                    fg=self.colors['dark'],
                    state='normal'
                )
            else:
                # 禁用不支持的格式
                btn.config(
                    bg=self.colors['border'],
                    fg=self.colors['muted'],
                    state='disabled'
                )
                
        # 清除当前选择
        self.target_format.set("")
        
        # 记录日志
        if supported_formats:
            formats_text = ", ".join(supported_formats)
            self.log_message(f"💡 当前文件支持转换为: {formats_text}")
        else:
            source_ext = os.path.splitext(source_path)[1].lower()
            self.log_message(f"❌ 不支持的文件格式: {source_ext}")
        
    def setup_log_panel(self, parent):
        """设置日志面板"""
        # 内边距容器
        container = tk.Frame(parent, bg=self.colors['white'])
        container.pack(fill='both', expand=True, padx=25, pady=25)
        
        # 标题
        title_label = tk.Label(container,
                              text="📋 转换日志",
                              font=('Helvetica', 16, 'bold'),
                              fg=self.colors['dark'],
                              bg=self.colors['white'])
        title_label.pack(anchor='w', pady=(0, 20))
        
        # 日志文本区域
        log_frame = tk.Frame(container, bg=self.colors['white'])
        log_frame.pack(fill='both', expand=True)
        
        # 创建文本框和滚动条
        self.log_text = tk.Text(log_frame,
                               font=('Courier New', 10),
                               bg=self.colors['dark'],
                               fg=self.colors['light'],
                               insertbackground=self.colors['light'],
                               relief='solid',
                               borderwidth=1,
                               padx=15,
                               pady=15,
                               wrap='word',
                               height=20)
        
        scrollbar = tk.Scrollbar(log_frame, orient='vertical', command=self.log_text.yview)
        self.log_text.configure(yscrollcommand=scrollbar.set)
        
        self.log_text.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        # 添加欢迎信息
        self.log_message("🎉 欢迎使用现代文件转换器！")
        self.log_message("📝 支持的转换格式：")
        self.log_message("   • PDF ↔ DOCX, MD")
        self.log_message("   • 图片格式互转")
        self.log_message("   • 表格格式互转")
        self.log_message("=" * 50)
        
    def create_footer(self, parent):
        """创建底部状态栏"""
        footer = tk.Frame(parent, bg=self.colors['border'], height=40)
        footer.pack(fill='x', side='bottom')
        footer.pack_propagate(False)
        
        # 状态标签
        self.status_label = tk.Label(footer,
                                    text="✅ 准备就绪",
                                    font=('Helvetica', 10),
                                    fg=self.colors['dark'],
                                    bg=self.colors['border'])
        self.status_label.pack(side='left', padx=20, pady=10)
        
        # 时间标签
        self.time_label = tk.Label(footer,
                                  text="",
                                  font=('Helvetica', 10),
                                  fg=self.colors['muted'],
                                  bg=self.colors['border'])
        self.time_label.pack(side='right', padx=20, pady=10)
        
        # 更新时间
        self.update_time()
        
    def update_time(self):
        """更新时间显示"""
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.time_label.config(text=current_time)
        self.root.after(1000, self.update_time)
        
    def select_format(self, format_name):
        """选择格式"""
        # 检查按钮是否可用
        if format_name in self.format_buttons:
            btn = self.format_buttons[format_name]
            if btn['state'] == 'disabled':
                self.log_message(f"❌ {format_name} 格式不支持当前文件类型")
                return
                
        self.target_format.set(format_name)
        
        # 更新按钮样式
        for fmt, btn in self.format_buttons.items():
            if btn['state'] == 'normal':  # 只更新可用按钮的样式
                if fmt == format_name:
                    btn.config(bg=self.colors['secondary'], 
                              fg=self.colors['white'],
                              borderwidth=3)
                else:
                    btn.config(bg=self.colors['white'], 
                              fg=self.colors['dark'],
                              borderwidth=2)
                    
        self.log_message(f"📌 已选择目标格式: {format_name}")
        
    def browse_source(self):
        """浏览源文件"""
        try:
            filename = filedialog.askopenfilename(
                title="选择源文件",
                filetypes=[
                    ("所有支持的文件", "*.pdf *.docx *.jpg *.jpeg *.png *.gif *.bmp *.csv *.xlsx"),
                    ("文档文件", "*.pdf *.docx"),
                    ("图像文件", "*.jpg *.jpeg *.png *.gif *.bmp"),
                    ("表格文件", "*.csv *.xlsx"),
                    ("所有文件", "*.*")
                ]
            )
            if filename:
                self.source_path.set(filename)
                display_name = os.path.basename(filename)
                if len(display_name) > 40:
                    display_name = display_name[:37] + "..."
                self.source_display.config(text=f"📄 {display_name}", fg=self.colors['dark'])
                self.log_message(f"📂 已选择源文件: {os.path.basename(filename)}")
                
                # 更新格式按钮状态
                self.update_format_buttons(filename)
                
        except Exception as e:
            self.log_message(f"❌ 选择文件时发生错误: {str(e)}")
            
    def browse_output(self):
        """浏览输出路径"""
        try:
            if not self.target_format.get():
                messagebox.showwarning("警告", "请先选择目标格式")
                return
                
            filename = filedialog.asksaveasfilename(
                title="选择输出文件",
                defaultextension=f".{self.target_format.get().lower()}",
                filetypes=[(f"{self.target_format.get()} 文件", f"*.{self.target_format.get().lower()}")]
            )
            if filename:
                self.output_path.set(filename)
                display_name = os.path.basename(filename)
                if len(display_name) > 40:
                    display_name = display_name[:37] + "..."
                self.output_display.config(text=f"📁 {display_name}", fg=self.colors['dark'])
                self.log_message(f"📁 已设置输出路径: {os.path.basename(filename)}")
        except Exception as e:
            self.log_message(f"❌ 选择输出路径时发生错误: {str(e)}")
            
    def log_message(self, message):
        """记录日志消息"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        formatted_message = f"[{timestamp}] {message}"
        self.log_text.insert(tk.END, formatted_message + "\n")
        self.log_text.see(tk.END)
        self.root.update_idletasks()
        
    def start_conversion(self):
        """开始转换"""
        if not self.source_path.get():
            messagebox.showerror("错误", "请选择源文件")
            return
            
        if not self.target_format.get():
            messagebox.showerror("错误", "请选择目标格式")
            return
            
        # 如果没有设置输出路径，自动生成
        if not self.output_path.get():
            source_file = self.source_path.get()
            base_name = os.path.splitext(os.path.basename(source_file))[0]
            output_dir = os.path.dirname(source_file)
            output_file = os.path.join(output_dir, f"{base_name}.{self.target_format.get().lower()}")
            self.output_path.set(output_file)
            
        # 在新线程中执行转换
        self.convert_btn.config(state='disabled', text="⏳ 转换中...")
        self.progress.start()
        self.status_label.config(text="🔄 正在转换...")
        self.log_message("🚀 开始转换...")
        
        thread = threading.Thread(target=self.convert_file)
        thread.daemon = True
        thread.start()
        
    def convert_file(self):
        """转换文件"""
        try:
            success = self.converter.convert(
                self.source_path.get(),
                self.output_path.get(),
                self.target_format.get()
            )
            
            if success:
                self.log_message("✅ 转换成功完成!")
                self.log_message(f"📄 输出文件: {os.path.basename(self.output_path.get())}")
                self.root.after(0, lambda: messagebox.showinfo("成功", "🎉 文件转换完成！"))
                self.root.after(0, lambda: self.status_label.config(text="✅ 转换完成"))
            else:
                self.log_message("❌ 转换失败!")
                self.root.after(0, lambda: messagebox.showerror("错误", "❌ 文件转换失败"))
                self.root.after(0, lambda: self.status_label.config(text="❌ 转换失败"))
                
        except Exception as e:
            error_msg = f"转换过程中发生错误: {str(e)}"
            self.log_message(f"❌ {error_msg}")
            self.root.after(0, lambda: messagebox.showerror("错误", error_msg))
            self.root.after(0, lambda: self.status_label.config(text="❌ 转换失败"))
            
        finally:
            self.root.after(0, self.conversion_finished)
            
    def conversion_finished(self):
        """转换完成"""
        self.progress.stop()
        self.convert_btn.config(state='normal', text="🚀 开始转换")


def main():
    root = tk.Tk()
    app = ModernFileConverterGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()