#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    my_dict = {
        "positive" : 0,
        "negative" : 0,
        "zeros" : 0
    }
    for i in arr:
        if i > 0:
            my_dict["positive"] +=1
        elif i < 0:
            my_dict["negative"] +=1
        else:
            my_dict["zeros"] +=1
    
    print (my_dict)

    print("{:.6f}".format(my_dict["positive"]/len(arr)))
    print("{:.6f}".format(my_dict["negative"]/len(arr)))
    print("{:.6f}".format(my_dict["zeros"]/len(arr)))
    

if __name__ == '__main__':
    
    #n = int(input())
    #arr = list(map(int, input().rstrip().split()))

    ''' Input:
    6
    -4 3 -9 0 4 1
    '''

    ''' Output:
    0.500000
    0.333333
    0.166667
    '''
    arr = [-4, 3, -9, 0, 4, 1]
    plusMinus(arr)

    arr = [1, 2, 3, -1, -2, -3, 0, 0]
    plusMinus(arr)
