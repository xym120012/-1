from random import *
from numpy import *
a = []
for i in range(10):
    x = uniform(0.22, 0.28)
    x = x * 100
    x = round(x, 2)
    a.append(x)
print("模拟生成数据"),
for i in range(10):
    if i == 9:
        print(a[i])
    else:
        print(a[i], end=" ")

print(std(a, ddof=1))
i = 0
while 1:
    if abs(a[i] - std(a, ddof=1)) > 2:
        print("异常值:", end="")
        print(a[i], end=" ")
        a.remove(a[i])
        continue
    i += 1
    if i > 9:
        break

for i in range(len(a)):
    print(a[i], end=" ")
