from typing import List, Any

import generate
import matplotlib.pyplot as plt
import analyze

# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    # 解决图像中的'-'负号的乱码问题
    plt.rcParams['axes.unicode_minus'] = False
    data = []
    abnum_index = []
    abnum = []
    data = generate.outdata(20, 30, 50)
    analyze.outlier(data, abnum, abnum_index)
    print("模拟生成数据")
    analyze.print_data(data)
    print("异常值")
    analyze.print_data(abnum)

    plt.figure(figsize=(16, 6))  # 新建绘图
    plt.subplot(1, 3, 1)  # 第一个子图，直方图
    plt.hist(data, bins=10, edgecolor="g", histtype="bar", alpha=0.5)
    if not abnum:
        pass
    else:
        plt.hist(abnum, bins=10, edgecolor="r", histtype="bar", alpha=0.5)
    plt.title("Histogram - data analysis")
    plt.xlabel("Temperature")
    plt.ylabel("Rate")

    plt.subplot(1, 3, 2)  # 第二个子图，箱线图
    plt.boxplot(data, vert=False)
    if not abnum:
        pass
    else:
        plt.scatter(abnum, [1] * len(abnum), color='r', label='Outliers')
    plt.title("Boxplot - data analysis")
    plt.xlabel("Temperature")

    plt.subplot(1, 3, 3)  # 第三个子图，茎叶图
    plt.stem(range(len(data)), data)  # 茎叶图
    if not abnum:
        pass
    else:
        plt.stem(abnum_index, abnum, linefmt='--r', markerfmt='or', basefmt='gray')

    plt.show()
