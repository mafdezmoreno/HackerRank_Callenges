# https://www.hackerrank.com/challenges/dynamic-array/copy-from/205082572
import os
from operator import xor
#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    ultima_respuesta = 0
    #resultado = [[]]*n #Forma erronea. no funciona bien append luego
    resultado = []
    ultimas_respuestas = []
    for _ in range(n):
        resultado.append([])

    for lista in queries:
        index = (xor(lista[1],ultima_respuesta)%n)
        print(index, lista)
        if lista[0] == 1:
            resultado[index].append(lista[2])

        elif lista[0] == 2:
            print(lista[2]%(len(resultado[index])))
            ultima_respuesta = resultado[index][lista[2]%(len(resultado[index]))]
            ultimas_respuestas.append(ultima_respuesta)
        print(ultima_respuesta)
    print(resultado)
    return ultimas_respuestas


if __name__ == '__main__':
    '''
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))
    '''
    queries = []


    with open('DynamicArray_2.txt') as file:
        n, q = [int(x) for x in next(file).split()]
        #i = 0
        for line in file:
            #if i > 9:
            #    break
            queries.append([int(x) for x in line.split()])
            #i = i + 1

    
    #print (n,q)
    for i in queries:
        print (i)

    result = dynamicArray(n, queries)

    print(result)
    '''
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
    '''