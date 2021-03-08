#!/bin/python3

import math
import os
import random
import re
import sys

'''
This is a staircase of size 4 :
   #
  ##
 ###
####

'''

# Complete the staircase function below.
def staircase(n):

    for i in range(n-1,-1,-1):
        for j in range(n):
            if j>=i:
                print("#",end="")
            else:
                print(" ",end="")
        print(i,j)


if __name__ == '__main__':
    
    #n = int(input())

    staircase(4)
