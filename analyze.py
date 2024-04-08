import numpy as np


def print_data(numlist):
    print("模拟生成数据"),
    for i in range(len(numlist)):
        if i == len(numlist) - 1:
            print(numlist[i])
        else:
            print(numlist[i], end=" ")


def average(numlist):
    return np.average(numlist)


def standard(numlist):
    return np.std(numlist)


def outlier(numlist, abnum, abnum_index):
    i = 0
    while 1:
        if i > len(numlist) - 1:
            break
        if abs(numlist[i] - average(numlist)) > 2 * standard(numlist):
            print("异常值:", end="")
            print(numlist[i])
            abnum.append(numlist[i])
            abnum_index.append(i)
        i += 1
