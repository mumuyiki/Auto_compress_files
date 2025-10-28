import os
import zipfile
import multiprocessing
from math import ceil

# 配置项
source_dir = r"C:\Users\xuan\Desktop\file"
output_dir = r"C:\Users\xuan\Desktop\zipfiles"
max_size = 1024 * 1024 * 1024  # 每个ZIP最大1GB
num_workers = 6  # 核心数设定

def group_files_by_size(file_list, max_size):
    """将文件按体积分组"""
    groups = []
    current_group = []
    current_size = 0

    for filepath, size in file_list:
        if current_size + size > max_size and current_group:
            groups.append(current_group)
            current_group = []
            current_size = 0
        current_group.append((filepath, size))
        current_size += size
    if current_group:
        groups.append(current_group)
    return groups

def zip_worker(args):
    """压缩一个文件组为zip"""
    group_index, group_files = args
    zip_path = os.path.join(output_dir, f"part{group_index + 1}.zip")
    print(f"[+] 开始打包 part{group_index + 1}.zip，共 {len(group_files)} 个文件")
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i, (filepath, _) in enumerate(group_files, 1):
            arcname = os.path.relpath(filepath, source_dir)
            zipf.write(filepath, arcname)
            print(f"    - {arcname} ({i}/{len(group_files)})")
    print(f"[√] 完成打包 part{group_index + 1}.zip")

def main():
    # 获取所有文件
    all_files = []
    for root, _, files in os.walk(source_dir):
        for file in files:
            full_path = os.path.join(root, file)
            size = os.path.getsize(full_path)
            all_files.append((full_path, size))

    # 分组
    file_groups = group_files_by_size(all_files, max_size)
    print(f"[INFO] 总共 {len(file_groups)} 个分组，将使用 {num_workers} 核心并行压缩")

    # 多进程压缩
    os.makedirs(output_dir, exist_ok=True)
    with multiprocessing.Pool(processes=num_workers) as pool:
        pool.map(zip_worker, enumerate(file_groups))

if __name__ == "__main__":
    main()
