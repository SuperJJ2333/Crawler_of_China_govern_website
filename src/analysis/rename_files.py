import os
import pandas as pd
import shutil

def rename_autonomous_regions(base_dir):
    """
    重命名自治区文件夹并更新其中 Excel 文件的 province 字段
    base_dir: 基础目录
    """
    # 自治区映射字典
    autonomous_regions = {
        '广西': '广西壮族自治区',
        '内蒙古': '内蒙古自治区',
        '宁夏': '宁夏回族自治区',
        '新疆': '新疆维吾尔自治区',
        '西藏': '西藏自治区'
    }
    
    try:
        # 确保目录存在
        if not os.path.exists(base_dir):
            print(f"目录 {base_dir} 不存在")
            return
        
        # 遍历所有文件夹
        for folder in os.listdir(base_dir):
            folder_path = os.path.join(base_dir, folder)
            
            # 检查是否是目录
            if not os.path.isdir(folder_path):
                continue
                
            # 检查是否需要重命名
            for old_name, new_name in autonomous_regions.items():
                if folder.startswith(old_name):
                    new_folder_path = os.path.join(base_dir, new_name)
                    
                    # 如果新文件夹已存在，先备份
                    if os.path.exists(new_folder_path):
                        backup_path = new_folder_path + '_backup'
                        shutil.move(new_folder_path, backup_path)
                        print(f"已备份原有文件夹: {new_folder_path} -> {backup_path}")
                    
                    # 重命名文件夹
                    os.rename(folder_path, new_folder_path)
                    print(f"重命名文件夹: {folder} -> {new_name}")
                    
                    # 更新文件夹中的 Excel 文件
                    for file in os.listdir(new_folder_path):
                        if file.endswith('.xlsx'):
                            file_path = os.path.join(new_folder_path, file)
                            try:
                                # 读取 Excel 文件
                                df = pd.read_excel(file_path)
                                
                                # 如果存在 province 列，更新内容
                                if 'province' in df.columns:
                                    df['province'] = df['province'].replace(old_name, new_name)
                                    
                                    # 保存更新后的文件
                                    df.to_excel(file_path, index=False)
                                    print(f"更新文件: {file} 中的 province 字段")
                                    
                            except Exception as e:
                                print(f"处理文件 {file} 时出错: {str(e)}")
                    
                    break
        
        print("处理完成！")
        
    except Exception as e:
        print(f"发生错误: {str(e)}")

if __name__ == "__main__":
    base_dir = r'E:\pythonProject\outsource\Crawler_of_China_govern_website\output\latest_total_time_range_data'
    rename_autonomous_regions(base_dir)
                              