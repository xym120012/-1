import generate
import matplotlib.pyplot as plt
import analyze
# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':


    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    # 解决图像中的'-'负号的乱码问题
    plt.rcParams['axes.unicode_minus'] = False

    a = generate.mudata_generate(20, 30, 50)
    abnum_index = []
    abnum = []

    analyze.print_data(a)
    analyze.outlier(a, abnum, abnum_index)
    print(abnum)

    plt.hist(a, bins=10, edgecolor="r", histtype="bar", alpha=0.5)

    plt.title("data analyze")
    plt.xlabel("temperature")
    plt.ylabel("rate")

    plt.figure()  # 新建绘图
    plt.grid()  # 显示网格
    # plt.plot(range(len(a)), a)
    # plt.scatter(n,x,c='b',marker = "<") #散点图
    plt.stem(range(len(a)), a)  # 茎叶图
    if not abnum:
        pass
    else:
        plt.stem(abnum_index, abnum, linefmt='--c2', markerfmt='<r', basefmt="-c2")

    plt.show()
