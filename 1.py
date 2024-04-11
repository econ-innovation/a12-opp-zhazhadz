# 打开文件
with open('qje2014_2023.txt', 'r') as f:
    # 读取第一行（标题行）
    titles = f.readline().strip().split('\t')
    
    # 创建一个字典来存储数据
    data = {title: [] for title in titles}
    
    # 逐行读取数据
    for line in f:
        # 分割每一行的数据
        values = line.strip().split('\t')
        
        # 将数据添加到字典
        for title, value in zip(titles, values):
            data[title].append(value)

