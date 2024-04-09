import numpy as np

def print_data(numlist):

    for i in range(len(numlist)):
        if i == len(numlist) - 1:
            print(numlist[i])
        else:
            print(numlist[i], end=" ")



def outlier(numlist, abnum, abnum_index):

    for i in range(len(numlist)):
        if abs(numlist[i] - np.average(numlist)) > 2 * np.std(numlist):
            abnum.append(numlist[i])
            abnum_index.append(i)


