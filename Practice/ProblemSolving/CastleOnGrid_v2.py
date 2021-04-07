# https://www.hackerrank.com/challenges/castle-on-the-grid/problem?h_r=next-challenge&h_v=zen

import os
from collections import deque
import time
from heapq import heappop, heappush


clear = lambda: os.system('clear')

class Nodo:
    
    direccion = -1
    en_path = False
    giros = 0
    h = 0
    longitud = 0
    padre = None
    vertice_anterior = None
    
    def __init__(self, posicion=[0, 0], final=[0,0]):
        self.posicion = posicion
        self.h = self.distancia(final)

    def update(self):
        self.f = self.h + self.giros
        if self.padre != None:
            self.longitud = self.padre.longitud + 1
            if(self.padre.direccion == -1):
                self.giros = self.padre.giros
            elif (self.direccion != self.padre.direccion):
                self.giros = self.padre.giros + 1
            else:
                self.giros = self.padre.giros
    
    def distancia(self, b):
        return abs(self.posicion[0] - b[0]) + abs(self.posicion[1] - b[1])

class Mapa:
    mapa = []
    inicio = None
    final = None
    def __init__ (self, grid, inicio, final):
        
        self.mapa.append([None]*(len(grid[0])+2))
        for y in range(len(grid)):
                temp = []
                temp.append(None)
                for x in range(len(grid[y])):
                    if grid[y][x] == 'X':
                        temp.append(None)
                    else:
                        temp.append(Nodo([x, y],final))
                temp.append(None)
                self.mapa.append(temp)
        self.mapa.append([None]*(len(grid[0])+2))
        
        self.inicio = self.mapa[inicio[1]+1][inicio[0]+1]
        self.final = self.mapa[final[1]+1][final[0]+1]
    
    def reinicar_camino(self):
        for y in range(len(self.mapa)):
            for x in range(len(self.mapa[y])):
                if self.mapa[y][x] != None:
                    self.mapa[y][x].en_path = False

    def imprime_mapa_h(self):
        for y in range(len(self.mapa)):
            for x in range(len(self.mapa[y])):
                if self.mapa[y][x] == None:
                    print(end="# ")
                else:
                    print(self.mapa[y][x].h, end=" ")
            print()
    
    def imprime_mapa_recorrido(self):
        for y in range(len(self.mapa)):
            for x in range(len(self.mapa[y])):
                if self.mapa[y][x] == self.inicio:
                    print(end="I")
                elif self.mapa[y][x] == self.final:
                    print(end="F")
                elif self.mapa[y][x] == None:
                    print(end="#")
                elif self.mapa[y][x].en_path:
                    print(end=".")
                else:
                    print(end=" ")
            print()
    
    def imprimie_extremos(self):
        print()
        print("Inicio: ", end = " ")
        print(self.inicio.posicion)
        print("Final:  ", end = " ")
        print(self.final.posicion)
        print()

    def imprime_coordenadas(self):
        for y in range(len(self.mapa)):
            for x in range(len(self.mapa[y])):
                if self.mapa[y][x] == None:
                    print(end="   #    ")
                else:
                    print (self.mapa[y][x].posicion, end="  ")
            print()
    
    def introduce_camino(self, final):
        while True:
            if final.padre == None:
                break
            final.en_path = True
            final = final.padre



def vecinos_trasitables(mapa, curr_pos, inicio):


    # Anadir el tipo de movimiento que se produce (der, izq, baja, sub) para contabilizar los giros
    vecinos = []
    to_check = [
        mapa.mapa[curr_pos.posicion[1]+2][curr_pos.posicion[0]+1],
        mapa.mapa[curr_pos.posicion[1]][curr_pos.posicion[0]+1], 
        mapa.mapa[curr_pos.posicion[1]+1][curr_pos.posicion[0]+2], 
        mapa.mapa[curr_pos.posicion[1]+1][curr_pos.posicion[0]]
    ]

    #movimiento anterior
    if curr_pos != inicio:
        is_turn = False
        if curr_pos.posicion[1] != curr_pos.padre.posicion[1] and curr_pos.posicion[0] == curr_pos.padre.posicion[0]:
            prev_mov = 'horizontal'
        else:
            prev_mov = 'vertical'

    for i in to_check:
            
        if (i!=None):
            if curr_pos == inicio:
                is_turn = False
            else:
                #movimiento actual
                if curr_pos.posicion[1] != i.posicion[1] and curr_pos.posicion[0] == i.posicion[0]:
                    sig_mov = 'vertical'
                else:
                    sig_mov = 'horizontal'
                    
                # If we're not still moving in the same direction, we have turned.
                is_turn = not (prev_mov == sig_mov)

            vecinos.append((i, is_turn))

    return vecinos
 
def imprime_coord_camino(padre):
    if padre != None:
        print(padre.posicion, end =" ")
        imprime_coord_camino(padre.padre)

def intro_path(mapa, path):
    for element in path:
        mapa.mapa[path[0]+1][path[1]+1].en_recorrido = True

def get_path(actual):
    path = []
    posicion = actual.posicion
    path.append(posicion)
    while actual.padre!=None:
        actual = actual.padre
        path.append(actual.posicion)
    print("Recorrido: ")
    print (path)
    return path

def set_vertices(origen, final):
    actual = origen
    vertice = origen
    vertices = 0
    while True:
        if actual.padre == None:
            break
        if (actual.padre.posicion[0]!=vertice.posicion[0]):
            if (actual.padre.posicion[1]!=vertice.posicion[1]):
                vertice.vertice_anterior = actual
                vertice = actual
                vertices = vertices + 1
        actual = actual.padre
    return vertices
  
def print_path_vertices(origen):
    if (origen != None)and(origen.vertice_anterior != None):
        print(origen.posicion,  origen.giros, end ="; ")
        print_path_vertices(origen.vertice_anterior)

def get_path_vertices(inicio):
    path = []
    path.append(inicio.posicion)
    while inicio.vertice_anterior!=None:
        inicio = inicio.vertice_anterior
        path.append(inicio.posicion)
    print()
    print("Path Vertices: ")
    print (path)
    return path

#Obtiene el ultimo punto de giro para asignarselo como padre
def get_giro(hijo, padre):
    A = hijo.posicion
    while True:
        if padre.padre == None:
            break
        padre = padre.padre
        if (A[0]==(padre.posicion)[0])or(A[1]==(padre.posicion)[1]):
            break 
    return padre

# Devuelve el vecino con menos giros:
def menor_f(open):
    if len(open) == 0:
        return 0
    menor_index = 0
    for i in range(1,len(open)):
        #if (open[menor_index].giros+open[menor_index].longitud) > (open[i].giros+open[i].longitud):
        if (open[menor_index].giros> open[i].giros):
            menor_index = i
    return menor_index
    
def make_path(curr_pos: tuple, route: dict, nodo_final) -> tuple:
        """Creates list of coordinates representing turns in path.

        :param curr_pos: end point of path.
        :param route: dict of coordinates leading to curr_pos
        :return: tuple containing list of coordinates of turns, len(list of coordinates)
        """
        turn_coords = []
        x, path_length = 0, 1
        prev_pos = curr_pos

        if route.get(nodo_final) is None:
            return 'No path found.', []

        while route[curr_pos] is not None:
            curr_pos = route[curr_pos][1]

            if curr_pos[x] != prev_pos[x]:
                if x == 0:
                    x = 1
                else:
                    x = 0

                if prev_pos is not nodo_final:
                    turn_coords.append(prev_pos)

            prev_pos = curr_pos
            path_length += 1

        turn_coords.reverse()
        return len(turn_coords), path_length

# Complete the minimumMoves function below.
def minimumMoves(grid, startX, startY, goalX, goalY):

        # Keep track of where we've been.
        visited = set()
        mapa = Mapa(grid,[startX, startY],[goalX, goalY])
        # We'll keep track of the route and the number of turns to reach the curr_pos with a dict.
        # {(position): (turns_count, (previous-position))}
        route = {mapa.inicio: None}

        # turn_count is used to promote routes with fewer turns.
        turn_count = {mapa.inicio: 0}

        open_pos = []
        heappush(open_pos, (0, mapa.inicio))

        while open_pos:
            # Routes with fewest turns_so_far are up first in the priority queue.
            turns_so_far, curr_pos = heappop(open_pos)

            if curr_pos in visited:
                continue

            #prev = route[curr_pos]  # Always remember where you came from so we know if we've turned.
            visited.add(curr_pos)  # But keep moving forward. Never go back!

            neighbors_list = vecinos_trasitables(mapa, curr_pos, mapa.inicio)
            for pos, did_turn in neighbors_list:
                if pos in visited:
                    continue

                if turn_count.get(pos):  # Have we been here before?
                    # If so, lets update our turn_count with the route containing the fewest turns.
                    turn_count[pos] = min(turn_count[pos], turns_so_far + int(did_turn))
                else:
                    turn_count[pos] = turns_so_far + int(did_turn)

                # In any case add this place to the list of places to explore.
                heappush(open_pos, (turn_count[pos], pos))

                old_route = route.get(pos)  # Do we know of another way to get here?
                # If so, does the old_route take more turns than the current route to get to pos?
                if old_route and turn_count[pos] < old_route[0]:
                    # If pos can be reached in fewer turns by the current route, we overwrite the old route.
                    route[pos] = (turn_count[pos], curr_pos)
                if not old_route:
                    route[pos] = (turn_count[pos], curr_pos)

        # Wait until open_pos is exhausted to ensure a shorter path doesn't end our search prematurely.
        print (mapa.make_path(mapa.end_pos, route))
        return mapa.make_path(mapa.end_pos, route)


if __name__ == '__main__':
    
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    with open('CastleOnGrid_test_case_1.txt') as file:
    #with open('CastleOnGrid_test2.txt') as file:

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

        result = minimumMoves(grid, startY, startX, goalY, goalX)

        print(result)

    #fptr.write(str(result) + '\n')
    #fptr.close()
