#https://www.hackerrank.com/challenges/sparse-arrays/problem

import math
import os
import random
import re
import sys

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    recuento = []
    #print(strings)
    #print(queries)
    for i in range(len(queries)):
        #recuento.append(strings.count(queries[i]))
        print(strings.count(queries[i])
    #print(recuento)

if __name__ == '__main__':

    strings = ['abcde', 'sdaklfj', 'asdjf', 'na', 'basdn', 'sdaklfj', 'asdjf', 'na', 'asdjf', 'na', 'basdn', 'sdaklfj', 'asdjf']
    queries = ['abcde', 'sdaklfj', 'asdjf', 'na', 'basdn']

    matchingStrings(strings, queries)

    # Sample output:
    '''
    1
    3
    4
    3
    2
    '''