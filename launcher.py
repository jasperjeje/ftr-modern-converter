import tkinter as tk
from tkinter import messagebox
import sys
import os

def show_ui_selector():
    """显示UI选择器"""
    root = tk.Tk()
    root.title("🚀 文件转换器 - 界面选择")
    root.geometry("550x650")
    root.resizable(False, False)
    
    # 设置窗口居中
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (550 // 2)
    y = (root.winfo_screenheight() // 2) - (650 // 2)
    root.geometry(f"550x650+{x}+{y}")
    
    # 主框架
    main_frame = tk.Frame(root, bg='#f8fafc')
    main_frame.pack(fill='both', expand=True)
    
    # 头部区域
    header_frame = tk.Frame(main_frame, bg='#2563eb', height=120)
    header_frame.pack(fill='x')
    header_frame.pack_propagate(False)
    
    # 标题
    title_label = tk.Label(header_frame,
                          text="🚀 现代文件转换器",
                          font=('Helvetica', 24, 'bold'),
                          fg='white',
                          bg='#2563eb')
    title_label.pack(pady=(25, 5))
    
    # 副标题
    subtitle_label = tk.Label(header_frame,
                             text="多格式文件转换工具",
                             font=('Helvetica', 12),
                             fg='#bfdbfe',
                             bg='#2563eb')
    subtitle_label.pack(pady=(0, 25))
    
    # 内容区域
    content_frame = tk.Frame(main_frame, bg='#f8fafc')
    content_frame.pack(fill='both', expand=True, padx=40, pady=30)
    
    # 选择提示
    select_label = tk.Label(content_frame,
                           text="请选择界面风格",
                           font=('Helvetica', 16, 'bold'),
                           fg='#1e293b',
                           bg='#f8fafc')
    select_label.pack(pady=(0, 25))
    
    # 按钮容器
    button_frame = tk.Frame(content_frame, bg='#f8fafc')
    button_frame.pack(pady=20)
    
    # 选择按钮
    def launch_modern():
        root.destroy()
        try:
            from modern_ui import main as modern_main
            modern_main()
        except ImportError as e:
            messagebox.showerror("错误", f"无法启动现代界面: {e}")
    
    def launch_classic():
        root.destroy()
        try:
            from main import main as classic_main
            classic_main()
        except ImportError as e:
            messagebox.showerror("错误", f"无法启动经典界面: {e}")
    
    # 现代UI按钮卡片
    modern_card = tk.Frame(button_frame, bg='white', relief='solid', borderwidth=1)
    modern_card.pack(pady=(0, 20), padx=20, fill='x')
    
    modern_btn = tk.Button(modern_card,
                          text="🎨 现代界面",
                          command=launch_modern,
                          font=('Helvetica', 14, 'bold'),
                          bg='#2563eb',
                          fg='white',
                          activebackground='#1d4ed8',
                          activeforeground='white',
                          relief='flat',
                          padx=30,
                          pady=20,
                          cursor='hand2')
    modern_btn.pack(fill='x', padx=15, pady=(15, 5))
    
    modern_desc = tk.Label(modern_card,
                          text="✨ 推荐选择 ✨\n现代化设计，更美观的界面体验\n支持PDF转Markdown等新功能",
                          font=('Helvetica', 11),
                          fg='#64748b',
                          bg='white',
                          justify='center')
    modern_desc.pack(pady=(0, 15))
    
    # 经典UI按钮卡片
    classic_card = tk.Frame(button_frame, bg='white', relief='solid', borderwidth=1)
    classic_card.pack(pady=(0, 20), padx=20, fill='x')
    
    classic_btn = tk.Button(classic_card,
                           text="📄 经典界面",
                           command=launch_classic,
                           font=('Helvetica', 14, 'bold'),
                           bg='#64748b',
                           fg='white',
                           activebackground='#475569',
                           activeforeground='white',
                           relief='flat',
                           padx=30,
                           pady=20,
                           cursor='hand2')
    classic_btn.pack(fill='x', padx=15, pady=(15, 5))
    
    classic_desc = tk.Label(classic_card,
                           text="简洁经典的界面风格\n保持原有的简单操作体验",
                           font=('Helvetica', 11),
                           fg='#64748b',
                           bg='white',
                           justify='center')
    classic_desc.pack(pady=(0, 15))
    
    # 功能特性介绍
    features_frame = tk.Frame(content_frame, bg='#f1f5f9', relief='solid', borderwidth=1)
    features_frame.pack(fill='x', pady=(20, 0), padx=20)
    
    features_title = tk.Label(features_frame,
                             text="🚀 主要功能特性",
                             font=('Helvetica', 13, 'bold'),
                             fg='#1e293b',
                             bg='#f1f5f9')
    features_title.pack(pady=(15, 10))
    
    features_text = tk.Label(features_frame,
                            text="📄 文档转换: PDF ↔ DOCX ↔ Markdown (新增!)\n"
                                 "🖼️  图像转换: JPG/PNG/GIF/BMP 互转 + PDF\n"
                                 "📊 表格转换: CSV ↔ XLSX ↔ PDF\n"
                                 "✨ 智能识别: 自动识别标题和列表结构\n"
                                 "🎨 现代设计: 优化界面，提升用户体验\n"
                                 "⚡ 一键转换: 简单三步完成文件转换",
                            font=('Helvetica', 10),
                            fg='#475569',
                            bg='#f1f5f9',
                            justify='left')
    features_text.pack(pady=(0, 15))
    
    # 底部提示
    footer_frame = tk.Frame(main_frame, bg='#e2e8f0', height=50)
    footer_frame.pack(fill='x', side='bottom')
    footer_frame.pack_propagate(False)
    
    footer_label = tk.Label(footer_frame,
                           text="💡 提示: 首次使用建议选择现代界面体验新功能",
                           font=('Helvetica', 10),
                           fg='#64748b',
                           bg='#e2e8f0')
    footer_label.pack(expand=True)
    
    root.mainloop()

if __name__ == "__main__":
    show_ui_selector()