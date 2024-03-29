from random import *
from numpy import *
from matplotlib import *
a = []
for i in range(9):
    x = uniform(0.20, 0.28)
    x = x * 100
    x = round(x, 2)
    a.append(x)
a.append(33.2)
print("模拟生成数据"),
for i in range(10):
    if i == 9:
        print(a[i])
    else:
        print(a[i], end=" ")

a_std = std(a, ddof=1)
a_arg = average(a)
i = 0
while 1:
    if i > len(a)-1:
        break
    if abs(a[i] - a_arg) > 2 * a_std:
        print("异常值:", end="")
        print(a[i])
        a.remove(a[i])
        continue
    i += 1

print(f"均值", a_arg)
print(f"标准差", a_std)
for i in range(len(a)):
    print(a[i], end=" ")
