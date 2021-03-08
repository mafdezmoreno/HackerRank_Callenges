import numpy as np

input_1 =      [[1, 2, 3, 0, 0, 0], 
                [0, 4, 0, 0, 0, 0],
                [5, 6, 7, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0]]

input_1_np = np.array(input_1)

print(input_1_np)

# Complete the hourglassSum function below.
def hourglassSum(arr):

    suma_maxima = 0
    for x in range(0,4):
        for y in range(0,4):
            temp = 0
            for i in range(x,x+3):
                for j in range(y,y+3):
                    if (((j-y)==0)or((j-y)==2))and(1==(i-x)):
                        print (end = "  ")
                        continue
                    print(arr[i][j],end=" ")
                    temp += arr[i][j]
                print()
            print(temp)
            if temp>suma_maxima:
                suma_maxima = temp
        print()
    print(suma_maxima)

    return suma_maxima

if __name__ == '__main__':

    result = hourglassSum(input_1)