import os
import pandas as pd
import shutil
from datetime import datetime

def merge_xlsx_files(source_file, target_file):
    """
    合并两个Excel文件，检查title列的重复性。
    
    参数:
    source_file: str, 源文件路径
    target_file: str, 目标文件路径
    
    返回:
    bool: 合并是否成功
    """
    try:
        # 读取两个Excel文件
        print(f"正在读取源文件: {source_file}")
        df_source = pd.read_excel(source_file)
        print(f"源文件列名: {df_source.columns.tolist()}")
        
        print(f"正在读取目标文件: {target_file}")
        df_target = pd.read_excel(target_file)
        print(f"目标文件列名: {df_target.columns.tolist()}")
        
        # 检查目标文件是否为空
        if len(df_target) == 0:
            print(f"目标文件为空，直接使用源文件")
            shutil.copy2(source_file, target_file)
            return True
        
        # 确保两个DataFrame都有title列
        if 'title' not in df_source.columns:
            print(f"源文件缺少title列")
            return False
        if 'title' not in df_target.columns:
            print(f"目标文件缺少title列")
            return False
            
        # 合并数据框并删除重复的title
        print(f"合并前源文件行数: {len(df_source)}")
        print(f"合并前目标文件行数: {len(df_target)}")
        
        df_merged = pd.concat([df_source, df_target], ignore_index=True)
        print(f"合并后总行数: {len(df_merged)}")
        
        # 检查重复的title
        duplicates = df_merged[df_merged.duplicated(subset=['title'], keep=False)]
        if not duplicates.empty:
            print(f"发现 {len(duplicates)} 个重复的title")
            print("重复的title示例:")
            print(duplicates['title'].head())
        
        df_merged = df_merged.drop_duplicates(subset=['title'])
        print(f"去重后行数: {len(df_merged)}")
        
        # 保存合并后的文件
        print(f"正在保存合并结果到: {target_file}")
        df_merged.to_excel(target_file, index=False)
        print("保存成功")
        return True
        
    except Exception as e:
        print(f"合并文件时出错:")
        print(f"错误类型: {type(e).__name__}")
        print(f"错误信息: {str(e)}")
        print(f"源文件: {source_file}")
        print(f"目标文件: {target_file}")
        
        # 尝试单独读取每个文件以定位问题
        try:
            df_test = pd.read_excel(source_file)
            print(f"源文件可以正常读取，行数: {len(df_test)}")
        except Exception as e1:
            print(f"源文件读取失败: {str(e1)}")
            
        try:
            df_test = pd.read_excel(target_file)
            print(f"目标文件可以正常读取，行数: {len(df_test)}")
            
            # 如果目标文件为空，直接使用源文件
            if len(df_test) == 0:
                print(f"目标文件为空，直接使用源文件")
                shutil.copy2(source_file, target_file)
                return True
                
        except Exception as e2:
            print(f"目标文件读取失败: {str(e2)}")
            
        return False

def copy_directory(src, dst):
    """
    复制整个目录及其内容
    
    参数:
    src: str, 源目录
    dst: str, 目标目录
    
    返回:
    bool: 复制是否成功
    """
    try:
        if not os.path.exists(dst):
            os.makedirs(dst)
            
        # 复制目录中的所有文件
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            
            if os.path.isdir(s):
                copy_directory(s, d)
            else:
                shutil.copy2(s, d)
                
        return True
    except Exception as e:
        print(f"复制目录失败: {str(e)}")
        return False

def compare_xlsx_sizes(before_dir, after_dir):
    """
    比较两个目录下同名Excel文件的大小，并根据需要复制或合并文件。
    
    参数:
    before_dir: str, 处理前的文件目录
    after_dir: str, 处理后的文件目录
    
    返回:
    None, 生成比较报告文件
    """
    
    print(f"开始处理目录:")
    print(f"源目录: {before_dir}")
    print(f"目标目录: {after_dir}")
    
    # 检查目录是否存在，如果after_dir不存在则创建
    if not os.path.exists(before_dir):
        print("源目录不存在，请检查路径")
        return
    if not os.path.exists(after_dir):
        os.makedirs(after_dir)
        print(f"创建目标目录: {after_dir}")
    
    # 存储比较结果
    comparison_results = []
    errors = []
    processed_files = []  # 记录已处理的文件
    
    # 首先检查before_dir中的文件夹是否存在于after_dir中
    before_dirs = [d for d in os.listdir(before_dir) if os.path.isdir(os.path.join(before_dir, d))]
    for dir_name in before_dirs:
        before_subdir = os.path.join(before_dir, dir_name)
        after_subdir = os.path.join(after_dir, dir_name)
        
        # 如果after_dir中不存在该文件夹，直接复制整个文件夹
        if not os.path.exists(after_subdir):
            print(f"\n目标目录不存在子目录: {dir_name}，执行整个目录复制")
            if copy_directory(before_subdir, after_subdir):
                print(f"复制目录成功: {dir_name}")
                
                # 统计复制的文件数量和大小
                copied_files = []
                total_size_before = 0
                total_size_after = 0
                
                for root, _, files in os.walk(before_subdir):
                    for file in files:
                        if file.endswith('.xlsx'):
                            rel_path = os.path.relpath(root, before_dir)
                            file_path = os.path.join(root, file)
                            copied_files.append(os.path.join(rel_path, file))
                            total_size_before += os.path.getsize(file_path)
                
                for root, _, files in os.walk(after_subdir):
                    for file in files:
                        if file.endswith('.xlsx'):
                            file_path = os.path.join(root, file)
                            total_size_after += os.path.getsize(file_path)
                
                # 添加到比较结果
                comparison_results.append({
                    '相对路径': f"{dir_name}/ (整个目录)",
                    '处理前大小(MB)': round(total_size_before / (1024 * 1024), 2),
                    '处理后大小(MB)': round(total_size_after / (1024 * 1024), 2),
                    '大小变化(MB)': 0,
                    '变化百分比(%)': 0,
                    '操作': f'复制目录 ({len(copied_files)}个文件)'
                })
            else:
                print(f"复制目录失败: {dir_name}")
                errors.append(f"复制目录失败: {dir_name}")
    
    # 遍历before目录
    for root, dirs, files in os.walk(before_dir):
        # 只处理xlsx文件
        xlsx_files = [f for f in files if f.endswith('.xlsx')]
        
        if xlsx_files:  # 如果当前目录有xlsx文件
            print(f"\n处理目录: {root}")
            print(f"发现 {len(xlsx_files)} 个xlsx文件")
        
        for file in xlsx_files:
            try:
                # 获取相对路径
                rel_path = os.path.relpath(root, before_dir)
                # 构建对应的after目录路径
                after_root = os.path.join(after_dir, rel_path)
                
                before_file_path = os.path.join(root, file)
                after_file_path = os.path.join(after_root, file)
                
                print(f"\n处理文件: {file}")
                print(f"源文件路径: {before_file_path}")
                print(f"目标文件路径: {after_file_path}")
                
                # 确保目标目录存在
                if not os.path.exists(after_root):
                    os.makedirs(after_root)
                    print(f"创建目标子目录: {after_root}")
                
                # 如果after目录中不存在该文件，直接复制
                if not os.path.exists(after_file_path):
                    print(f"目标文件不存在，执行复制操作")
                    os.makedirs(os.path.dirname(after_file_path), exist_ok=True)
                    shutil.copy2(before_file_path, after_file_path)
                    
                    if os.path.exists(after_file_path):
                        print(f"复制成功: {after_file_path}")
                    else:
                        print(f"复制失败: {after_file_path}")
                        
                    comparison_results.append({
                        '相对路径': os.path.join(rel_path, file),
                        '处理前大小(MB)': round(os.path.getsize(before_file_path) / (1024 * 1024), 2),
                        '处理后大小(MB)': round(os.path.getsize(after_file_path) / (1024 * 1024), 2),
                        '大小变化(MB)': 0,
                        '变化百分比(%)': 0,
                        '操作': '复制'
                    })
                else:
                    print(f"目标文件已存在，检查大小")
                    
                    # 检查目标文件是否为空
                    try:
                        df_target = pd.read_excel(after_file_path)
                        if len(df_target) == 0:
                            print(f"目标文件为空，直接使用源文件")
                            shutil.copy2(before_file_path, after_file_path)
                            
                            comparison_results.append({
                                '相对路径': os.path.join(rel_path, file),
                                '处理前大小(MB)': round(os.path.getsize(before_file_path) / (1024 * 1024), 2),
                                '处理后大小(MB)': round(os.path.getsize(after_file_path) / (1024 * 1024), 2),
                                '大小变化(MB)': 0,
                                '变化百分比(%)': 0,
                                '操作': '替换空文件'
                            })
                            continue
                    except Exception as e:
                        print(f"检查目标文件是否为空时出错: {str(e)}")
                    
                    # 获取文件大小（以MB为单位）
                    before_size = os.path.getsize(before_file_path) / (1024 * 1024)
                    after_size = os.path.getsize(after_file_path) / (1024 * 1024)
                    
                    print(f"源文件大小: {round(before_size, 2)}MB")
                    print(f"目标文件大小: {round(after_size, 2)}MB")
                    
                    # 如果after目录中的文件较小，需要合并
                    if after_size < before_size:
                        print(f"目标文件较小，执行合并操作")
                        if merge_xlsx_files(before_file_path, after_file_path):
                            new_size = os.path.getsize(after_file_path) / (1024 * 1024)
                            size_diff = new_size - before_size
                            change_percent = (size_diff / before_size) * 100 if before_size > 0 else float('inf')
                            
                            print(f"合并后文件大小: {round(new_size, 2)}MB")
                            
                            comparison_results.append({
                                '相对路径': os.path.join(rel_path, file),
                                '处理前大小(MB)': round(before_size, 2),
                                '处理后大小(MB)': round(new_size, 2),
                                '大小变化(MB)': round(size_diff, 2),
                                '变化百分比(%)': round(change_percent, 2),
                                '操作': '合并'
                            })
                        else:
                            print(f"合并失败")
                            errors.append(f"合并文件失败: {os.path.join(rel_path, file)}")
                    else:
                        print(f"目标文件大小合适，无需处理")
                        # 文件已存在且大小合适，记录比较结果
                        size_diff = after_size - before_size
                        change_percent = (size_diff / before_size) * 100 if before_size > 0 else float('inf')
                        
                        comparison_results.append({
                            '相对路径': os.path.join(rel_path, file),
                            '处理前大小(MB)': round(before_size, 2),
                            '处理后大小(MB)': round(after_size, 2),
                            '大小变化(MB)': round(size_diff, 2),
                            '变化百分比(%)': round(change_percent, 2),
                            '操作': '无'
                        })
                
                processed_files.append(after_file_path)
                    
            except Exception as e:
                print(f"处理文件出错: {str(e)}")
                errors.append(f"处理文件时出错 {file}: {str(e)}")
    
    # 如果没有比较结果，直接返回
    if not comparison_results and not errors:
        print("未找到可比较的文件")
        return
    
    # 创建报告目录
    report_dir = os.path.join(os.path.dirname(before_dir), "reports")
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)
    
    # 生成报告文件名
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = os.path.join(report_dir, f"size_comparison_report_{timestamp}.xlsx")
    
    # 创建DataFrame并保存为Excel
    if comparison_results:
        df = pd.DataFrame(comparison_results)
        
        # 计算总体统计
        total_stats = {
            '相对路径': '总计',
            '处理前大小(MB)': round(df['处理前大小(MB)'].sum(), 2),
            '处理后大小(MB)': round(df['处理后大小(MB)'].sum(), 2),
            '大小变化(MB)': round(df['大小变化(MB)'].sum(), 2),
            '变化百分比(%)': round((df['大小变化(MB)'].sum() / df['处理前大小(MB)'].sum()) * 100, 2),
            '操作': ''
        }
        
        # 添加总计行
        df = pd.concat([df, pd.DataFrame([total_stats])], ignore_index=True)
        
        # 保存Excel文件
        with pd.ExcelWriter(report_path, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name='文件大小比较', index=False)
            
            # 如果有错误，添加错误sheet
            if errors:
                pd.DataFrame({'错误信息': errors}).to_excel(writer, sheet_name='错误记录', index=False)
    
    # 打印统计信息
    print(f"\n处理完成！")
    print(f"比较文件数: {len(comparison_results)}")
    print(f"错误数: {len(errors)}")
    print(f"详细报告已保存至: {report_path}")
    
    # 如果有错误，打印错误信息
    if errors:
        print("\n错误记录:")
        for error in errors:
            print(f"- {error}")

if __name__ == "__main__":
    # 使用示例
    # 获取当前文件的绝对路径
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # 构建目录路径
    after_dir = os.path.abspath(os.path.join(current_dir, "..", "..", "output", "latest_total_time_range_data"))
    before_dir = os.path.abspath(os.path.join(current_dir, "..", "..", "output", "Total_time_range_data"))
    compare_xlsx_sizes(before_dir, after_dir)
