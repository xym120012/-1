from random import *
from numpy import *
import analyze
def mudata_generate(min: int, max: int, num: int):
    a = []
    for i in range(num):
        x = uniform(min, max)
        x = round(x, 2)
        a.append(x)
    return a

def outdata(min: int, max: int, num: int):
    abnum_index = []
    abnum = []
    while 1:
        a = mudata_generate(min, max, num)
        analyze.outlier(a, abnum, abnum_index)
        if len(abnum) >= 4:
            break
        abnum = []
        abnum_index = []
    return a

