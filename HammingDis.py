# 打开文件，替换 'your_file.txt' 为实际的文件路径
file_path = "/home/nina/Downloads/dataset_30278_3.txt"

# 初始化计数器
count = 0

with open(file_path, "r") as file:
    lines = file.readlines()

    # 确保文件至少有两行
    if len(lines) >= 2:
        # 比较每个字符
        for i in range(min(len(lines[0]), len(lines[1]))):
            # 如果两行对应位置的字符不同，计数器加1
            if lines[0][i] != lines[1][i]:
                count += 1

# 输出计数结果
print(count)
