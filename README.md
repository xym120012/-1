# 专业实验一
（1）模拟生成一组实验需要的传感器数据样本，这些数据可以是温度、湿度、压力等常见的传感器读数。
（2）异常检测算法实现：利用基本的统计学原理，如标准差规则（例如，识别那些超出均值±2标准差的值作为异常值）。	编写代码实现简单统计方法的异常检测，标记出数据中的异常点。
（3）数据可视化：使用数据可视化库（如Python matplotlib或seaborn）将原始数据和检测到的异常值进行可视化，以便直观展示分析结果。绘制数据分布的直方图或箱线图，辅助识别异常值。

a_std = std(a, ddof=1)
a_arg = average(a)
i = 0
while 1:
    if i > len(a)-1:
        break
    if abs(a[i] - a_arg) > 2 * a_std:
        print("异常值:", end="")
        print(a[i])
        abnum.append(a[i])
        abnum_index.append(i)
    i += 1

print(f"均值", a_arg)
print(f"标准差", a_std)
for i in range(len(a)):
    print(a[i], end=" ")



import numpy as np
import self


class data():
    def __init__(self, num, std, ave, abnum, abnum_index):
        self.num = num
        self.std = std
        self.ave = ave
        self.abnum = abnum
        self.abnum_index = abnum_index
    @property
    def average(self):
        return np.average(self.num)


    @property
    def standard(self):
        return np.std(self.num)


    def outlier(self):
        i: int = 0
        while 1:
            if i > len(self.num) - 1:
                break
            if abs(self.num[i] - self.average(self.num) ) > 2 * self.standard(self.num):
                print("异常值:", end="")
                print(self.num[i])
                self.abnum.append(self.num[i])
                self.abnum_index.append(i)
                i += 1
        
    