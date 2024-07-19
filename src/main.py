import os
from concurrent.futures import ProcessPoolExecutor
import subprocess


def run_script(script_path):
    """ 运行单个脚本文件 """
    try:
        # 使用Python命令执行脚本
        result = subprocess.run(['python', script_path], capture_output=True, text=True)
        print(f"执行完成: {script_path}\n输出:\n{result.stdout}")
    except Exception as e:
        print(f"执行错误: {script_path}\n错误信息:\n{str(e)}")


def main(folder_path, max_workers):
    # 获取所有.py文件
    scripts = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.py')]

    # 创建一个进程池执行器，最大并行进程数为max_workers
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        # 映射run_script函数到所有脚本文件上
        executor.map(run_script, scripts)


if __name__ == "__main__":
    # 设置文件夹路径和同时最大运行文件数
    folder_path = 'path_to_your_folder'
    max_workers = 4  # 同时最大运行脚本数
    main(folder_path, max_workers)
