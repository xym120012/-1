import generate
from numpy import *
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
# 解决图像中的'-'负号的乱码问题
plt.rcParams['axes.unicode_minus'] = False

a = generate.mudata_generate(22, 28, 50)
abnum_index = []
abnum = []

print("模拟生成数据"),
for i in range(len(a)):
    if i == len(a) - 1:
        print(a[i])
    else:
        print(a[i], end=" ")

a_std = std(a, ddof=1)
a_arg = average(a)
i = 0
while 1:
    if i > len(a)-1:
        break
    if abs(a[i] - a_arg) > 1.5 * a_std:
        print("异常值:", end="")
        print(a[i])
        abnum.append(a[i])
        abnum_index.append(i)
    i += 1

print(f"均值", a_arg)
print(f"标准差", a_std)
for i in range(len(a)):
    print(a[i], end=" ")



plt.hist(a, bins=10, edgecolor="r", histtype="bar", alpha=0.5)

plt.title("data analyze")
plt.xlabel("temperature")
plt.ylabel("rate")

plt.figure()  # 新建绘图
plt.grid()  # 显示网格
#plt.plot(range(len(a)), a)
# plt.scatter(n,x,c='b',marker = "<") #散点图
plt.stem(range(len(a)), a)  # 茎叶图
plt.stem(abnum_index, abnum, linefmt='--c2', markerfmt='<r', basefmt="-c2")
#plt.show()

plt.show()
