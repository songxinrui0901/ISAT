import os
import argparse
from concurrent.futures import ProcessPoolExecutor

def merge_single_file(file_name, folder1, folder2, output_dir):
    """合并单个同名文件"""
    path1 = os.path.join(folder1, file_name)
    path2 = os.path.join(folder2, file_name)
    output_path = os.path.join(output_dir, file_name)

    # 逐行读取文件，减少内存占用
    def read_file(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                yield line

    # 使用生成器拼接内容
    with open(output_path, 'w', encoding='utf-8') as f_out:
        for line in read_file(path1):
            f_out.write(line)
        for line in read_file(path2):
            f_out.write(line)

    print(f"合并完成：{file_name}")

def merge_txt_files_parallel(folder1, folder2, output_dir, max_workers=4):
    """使用多进程合并txt文件"""
    files1 = set(f for f in os.listdir(folder1) if f.endswith('.txt'))
    files2 = set(f for f in os.listdir(folder2) if f.endswith('.txt'))
    common_files = files1 & files2  # 找到同名的txt文件

    os.makedirs(output_dir, exist_ok=True)  # 确保输出目录存在

    # 使用多进程加速文件合并
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        for file_name in common_files:
            executor.submit(merge_single_file, file_name, folder1, folder2, output_dir)

    print(f"合并完成，共处理 {len(common_files)} 个文件。")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='高效合并两个文件夹中的同名txt文件')
    parser.add_argument('folder1', help='第一个文件夹路径')
    parser.add_argument('folder2', help='第二个文件夹路径')
    parser.add_argument('output_dir', help='合并后的输出文件夹路径')
    parser.add_argument('--workers', type=int, default=4, help='并行处理的进程数（默认4）')
    args = parser.parse_args()

    merge_txt_files_parallel(args.folder1, args.folder2, args.output_dir, args.workers)
