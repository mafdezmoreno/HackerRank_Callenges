# https://www.hackerrank.com/challenges/castle-on-the-grid/problem?h_r=next-challenge&h_v=zen

import os

# Complete the minimumMoves function below.
def minimumMoves(grid, startX, startY, goalX, goalY):
    print(grid)
    print(startX, startY, goalX, goalY)

if __name__ == '__main__':
    
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    with open('CastleOnGrid_test.txt') as file:

    #n = int(input())
        n = int(next(file))

        grid = []

        for _ in range(n):
            #grid_item = input()
            grid_item = next(file).split()
            grid.append(grid_item[0])

        #startXStartY = input().split()
        startXStartY = next(file).split()

        startX = int(startXStartY[0])

        startY = int(startXStartY[1])

        goalX = int(startXStartY[2])

        goalY = int(startXStartY[3])

        result = minimumMoves(grid, startX, startY, goalX, goalY)

    #fptr.write(str(result) + '\n')

    #fptr.close()
