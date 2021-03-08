# https://www.hackerrank.com/challenges/array-left-rotation/problem

from array import array as arr

'''
Sample Input
5 4
1 2 3 4 5

Sample Output
5 1 2 3 4
'''

def rotateLeft(d, arr, n):
    print(arr)
    if d > n:
        d = d%n
        print (d)
    return arr[d:] + arr[:d]

if __name__ == '__main__':

    with open('left_rotation.txt') as f:
        n, d = [int(x) for x in next(f).split()]
        temp =  [int(x) for x in next(f).split()]

    print (n,d)
    print (temp)

    result = rotateLeft(d, temp, n)

    print(result)