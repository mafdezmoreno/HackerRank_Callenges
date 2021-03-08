#https://www.hackerrank.com/challenges/crush/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

from datetime import datetime
import array

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
## Excede tiempo ejecución: 59    
    temp = [0]*n
    for rango in queries:
        for x in range(rango[0]-1,rango[1]):
            temp[x]+= rango[2]
            #print(x)
        #print(temp)
    return max(temp)

def arrayManipulation2(n, queries):
## Excede tiempo ejecución: 60    
    temp = [0]*n
    #print(temp)
    for rango in queries:
        #for x in range(rango[0]-1,rango[1]):
        temp = temp[:rango[0]-1] + [x+rango[2] for x in temp[rango[0]-1:rango[1]]] + temp[rango[1]:]
        #print(temp)
    return max(temp)

def arrayManipulation2(n, queries):
## Excede tiempo ejecución: 60    
    temp = [0]*n
    #print(temp)
    for rango in queries:
        #for x in range(rango[0]-1,rango[1]):
        temp = temp[:rango[0]-1] + (temp[rango[0]-1:rango[1]]+2) + temp[rango[1]:]
        #print(temp)
    return max(temp)

def arrayManipulation3(n, queries):
## Excede tiempo ejecución: 53 (pero no incrementa con rangos de datos mayores)   
    temp = [0]*(n+1)
    for rango in queries:
        temp[rango[0]-1] += rango[2]
        temp[rango[1]] -= rango[2]
        print(temp)
    
    acumulado = 0
    for i in range(len(temp)):
        acumulado += temp[i]
        temp[i] = acumulado
        
        print(acumulado, end= " ")
    print()
    print(temp)
    return max(temp)


def arrayManipulation4(n, queries):
## Excede tiempo ejecución: 53 (pero no incrementa con rangos de datos mayores)   
    temp = array.array('q', [0]*(n+1))
    for rango in queries:
        temp[rango[0]-1] += rango[2]
        temp[rango[1]] -= rango[2]
        print(temp)
    
    acumulado = 0
    for i in range(len(temp)):
        acumulado += temp[i]
        temp[i] = acumulado
        
        print(acumulado, end= " ")
    print()
    print(temp)
    return max(temp)


if __name__ == '__main__':

    startTime = datetime.now()
    n = 10
    queries = [[1, 5, 3], [4, 8, 7],[6, 9, 1]]
    
    result = arrayManipulation4(n, queries)
    print (result)
    
    n = 10
    queries = [[2, 6, 8] , [3, 5, 7], [1, 8, 1], [5,9,15]]
    result = arrayManipulation4(n, queries)
    print (result)
    
    print(datetime.now() - startTime)
    
    n = 5
    queries = [[1, 2, 100] , [2, 5, 100], [3, 4, 100]]
    result = arrayManipulation4(n, queries)
    print (result)
 