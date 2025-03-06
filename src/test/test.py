import os

def check_directories():
    source_dir = r'E:\pythonProject\outsource\Crawler_of_China_govern_website\output\Total_time_range_data'
    target_dir = r'E:\pythonProject\outsource\Crawler_of_China_govern_website\output\latest_total_time_range_data'
    
    # 检查源目录
    print("检查源目录:")
    if os.path.exists(source_dir):
        files = os.listdir(source_dir)
        print(f"源目录存在，包含文件数量: {len(files)}")
        print("文件列表:", files)
    else:
        print("源目录不存在")
    
    # 检查目标目录
    print("\n检查目标目录:")
    if os.path.exists(target_dir):
        files = os.listdir(target_dir)
        print(f"目标目录存在，包含文件数量: {len(files)}")
        print("文件列表:", files)
    else:
        print("目标目录不存在")

if __name__ == "__main__":
    check_directories()