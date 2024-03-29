from random import *
from numpy import *
def mudata_generate(min: int, max: int, num: int):
    a = []
    for i in range(num):
        x = uniform(min, max)
        x = round(x, 2)
        a.append(x)
    return a
