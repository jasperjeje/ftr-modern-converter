#!/usr/bin/env python3
"""
命令行版本的文件转换工具
"""

import os
import sys
import argparse
from file_converter import FileConverter


def main():
    parser = argparse.ArgumentParser(description='文件转换工具 - 命令行版本')
    parser.add_argument('source', help='源文件路径')
    parser.add_argument('output', help='输出文件路径')
    parser.add_argument('format', help='目标格式 (PDF, DOCX, JPG, PNG, GIF, BMP, CSV, XLSX)')
    
    args = parser.parse_args()
    
    # 检查源文件是否存在
    if not os.path.exists(args.source):
        print(f"错误: 源文件不存在: {args.source}")
        sys.exit(1)
    
    # 初始化转换器
    converter = FileConverter()
    
    print(f"开始转换: {args.source} -> {args.output}")
    print(f"目标格式: {args.format}")
    
    # 执行转换
    try:
        success = converter.convert(args.source, args.output, args.format)
        
        if success:
            print("✅ 转换成功!")
            print(f"输出文件: {args.output}")
        else:
            print("❌ 转换失败!")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ 转换过程中发生错误: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()