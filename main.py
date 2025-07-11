import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import threading
from file_converter import FileConverter


class FileConverterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("文件转换工具")
        self.root.geometry("600x400")
        self.root.resizable(True, True)
        
        self.converter = FileConverter()
        self.setup_ui()
        
    def setup_ui(self):
        # 主框架
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 配置网格权重
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # 源文件选择
        ttk.Label(main_frame, text="源文件:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.source_path = tk.StringVar()
        ttk.Entry(main_frame, textvariable=self.source_path, width=50).grid(row=0, column=1, sticky=(tk.W, tk.E), padx=5)
        ttk.Button(main_frame, text="浏览", command=self.browse_source).grid(row=0, column=2, padx=5)
        
        # 目标格式选择
        ttk.Label(main_frame, text="目标格式:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.target_format = tk.StringVar()
        self.format_combo = ttk.Combobox(main_frame, textvariable=self.target_format, 
                                       values=["PDF", "DOCX", "MD", "JPG", "PNG", "GIF", "BMP", "CSV", "XLSX"], 
                                       state="readonly")
        self.format_combo.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=5)
        
        # 输出路径选择
        ttk.Label(main_frame, text="输出路径:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.output_path = tk.StringVar()
        ttk.Entry(main_frame, textvariable=self.output_path, width=50).grid(row=2, column=1, sticky=(tk.W, tk.E), padx=5)
        ttk.Button(main_frame, text="浏览", command=self.browse_output).grid(row=2, column=2, padx=5)
        
        # 转换按钮
        self.convert_btn = ttk.Button(main_frame, text="开始转换", command=self.start_conversion)
        self.convert_btn.grid(row=3, column=1, pady=20)
        
        # 进度条
        self.progress = ttk.Progressbar(main_frame, mode='indeterminate')
        self.progress.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=10)
        
        # 状态标签
        self.status_label = ttk.Label(main_frame, text="准备就绪")
        self.status_label.grid(row=5, column=0, columnspan=3, pady=5)
        
        # 日志框架
        log_frame = ttk.LabelFrame(main_frame, text="转换日志", padding="5")
        log_frame.grid(row=6, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)
        main_frame.rowconfigure(6, weight=1)
        
        # 日志文本框
        self.log_text = tk.Text(log_frame, height=8, width=70)
        scrollbar = ttk.Scrollbar(log_frame, orient=tk.VERTICAL, command=self.log_text.yview)
        self.log_text.configure(yscrollcommand=scrollbar.set)
        
        self.log_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        log_frame.columnconfigure(0, weight=1)
        log_frame.rowconfigure(0, weight=1)
        
    def browse_source(self):
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
                self.update_format_options()
        except Exception as e:
            messagebox.showerror("错误", f"选择文件时发生错误: {str(e)}")
            
    def browse_output(self):
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
        except Exception as e:
            messagebox.showerror("错误", f"选择输出路径时发生错误: {str(e)}")
            
    def update_format_options(self):
        """更新格式选项"""
        source_file = self.source_path.get()
        if not source_file:
            return
            
        # 获取支持的目标格式
        supported_formats = self.converter.get_supported_target_formats(source_file)
        
        if supported_formats:
            self.format_combo['values'] = supported_formats
            # 记录支持的格式
            formats_text = ", ".join(supported_formats)
            self.log_message(f"支持的目标格式: {formats_text}")
        else:
            self.format_combo['values'] = []
            ext = os.path.splitext(source_file)[1].lower()
            self.log_message(f"不支持的文件格式: {ext}")
        
        # 清除当前选择
        self.target_format.set("")
        
    def log_message(self, message):
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.root.update_idletasks()
        
    def start_conversion(self):
        if not self.source_path.get():
            messagebox.showerror("错误", "请选择源文件")
            return
            
        if not self.target_format.get():
            messagebox.showerror("错误", "请选择目标格式")
            return
            
        if not self.output_path.get():
            messagebox.showerror("错误", "请选择输出路径")
            return
            
        # 在新线程中执行转换
        self.convert_btn.config(state='disabled')
        self.progress.start()
        self.status_label.config(text="转换中...")
        self.log_message(f"开始转换: {os.path.basename(self.source_path.get())}")
        
        thread = threading.Thread(target=self.convert_file)
        thread.daemon = True
        thread.start()
        
    def convert_file(self):
        try:
            success = self.converter.convert(
                self.source_path.get(),
                self.output_path.get(),
                self.target_format.get()
            )
            
            if success:
                self.log_message("转换成功!")
                self.root.after(0, lambda: messagebox.showinfo("成功", "文件转换完成!"))
                self.root.after(0, lambda: self.status_label.config(text="转换完成"))
            else:
                self.log_message("转换失败!")
                self.root.after(0, lambda: messagebox.showerror("错误", "文件转换失败"))
                self.root.after(0, lambda: self.status_label.config(text="转换失败"))
                
        except Exception as e:
            error_msg = f"转换过程中发生错误: {str(e)}"
            self.log_message(error_msg)
            self.root.after(0, lambda: messagebox.showerror("错误", error_msg))
            self.root.after(0, lambda: self.status_label.config(text="转换失败"))
            
        finally:
            self.root.after(0, self.conversion_finished)
            
    def conversion_finished(self):
        self.progress.stop()
        self.convert_btn.config(state='normal')


def main():
    root = tk.Tk()
    app = FileConverterGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()