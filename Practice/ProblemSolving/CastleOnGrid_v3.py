#https://github.com/srgnk/HackerRank/blob/master/data-structures/castle-on-the-grid.py
#!/usr/bin/env python3

import sys
from collections import deque

def is_safe(grid, x, y, distances):
    return x >= 0 and x < len(grid) and y >= 0 and y < len(grid) and distances[x][y] == -1 and grid[x][y] != 'X' 

def get_safe_moves(grid, node, distances):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    variants = []
    
    for di in directions:
        nunode = (node[0] + di[0], node[1] + di[1])
        while is_safe(grid, nunode[0], nunode[1], distances):
            variants.append(nunode)
            nunode = (nunode[0] + di[0], nunode[1] + di[1])
            
    return variants
            

def minimumMoves(grid, startX, startY, goalX, goalY):
    next_to_visit = deque()
    node = (startX, startY)
    next_to_visit.appendleft(node)
    distances = [[-1]*len(grid) for _ in range(len(grid))]
    distances[startX][startY] = 0
    
    while next_to_visit:
        node = next_to_visit.pop()
        #print("point = ({}, {})".format(node[0], node[1]))
        #for row in distances:
        #    print(row)
        #print()
        height = distances[node[0]][node[1]]
       
        variants = get_safe_moves(grid, node, distances)
        
        for var in variants:
            if var == (goalX, goalY):
                return height + 1
            distances[var[0]][var[1]] = height + 1
            next_to_visit.appendleft(var)
                
    return -1
    

if __name__ == '__main__':
    
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    with open('CastleOnGrid_test_case_0.txt') as file:
    #with open('CastleOnGrid_test2.txt') as file:

    #n = int(input())
        n = int(next(file))

        grid = []

        for _ in range(n):
            layer = list(next(file).strip())
            grid.append(layer)

        startX, startY, goalX, goalY = [int(i) for i in next(file).split()]

        result = minimumMoves(grid, startX, startY, goalX, goalY,)

        print("\nResultado: ")
        print(" \t \t", end = " ")
        print(result, "\n")

    #fptr.write(str(result) + '\n')
    #fptr.close()
