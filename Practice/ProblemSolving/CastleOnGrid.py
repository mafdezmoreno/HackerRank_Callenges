# https://www.hackerrank.com/challenges/castle-on-the-grid/problem?h_r=next-challenge&h_v=zen

import os
from collections import deque
import time

clear = lambda: os.system('clear')

class Nodo:
    
    direccion = -1
    f = 0
    en_path = False
    giros = 0
    padre = None
    vertice_anterior = None
    
    def __init__(self, posicion=[0, 0], final=[0,0]):
        self.posicion = posicion
        #self.h = self.distancia(final)

    def update(self):
        #self.f = self.giros + self.h
        if self.padre != None:
            if(self.direccion == -1):
                self.giros = self.padre.giros
            elif (self.direccion != self.padre.direccion):
                self.giros = self.padre.giros + 1
            else:
                self.giros = self.padre.giros

    # Distancia entre dos puntos.
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
                        temp.append(Nodo([x, y], final))
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
        if final != None:
            final.en_path = True
            self.introduce_camino(final.padre)


# Devuelve el vecino con menos giros:
def menor_f(open):
    if len(open) == 0:
        return 0
    menor_index = 0
    for i in range(1,len(open)):
        if open[menor_index].giros >= open[i].giros:
            menor_index = i
    return menor_index
    

def vecinos_trasitables(mapa, nodo, closed):

        # Anadir el tipo de movimiento que se produce (der, izq, baja, sub) para contabilizar los giros
        vecinos = []
        to_check = [
            mapa.mapa[nodo.posicion[1]+2][nodo.posicion[0]+1],
            mapa.mapa[nodo.posicion[1]][nodo.posicion[0]+1], 
            mapa.mapa[nodo.posicion[1]+1][nodo.posicion[0]+2], 
            mapa.mapa[nodo.posicion[1]+1][nodo.posicion[0]]
        ]
        j = 0
        for i in to_check:
            if (i!=None) :
                i.direccion = j
                if not(i in closed):
                    vecinos.append(i)
            j=j+1

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
    while True:
        if actual.padre == None:
            break
        if (actual.padre.posicion[0]!=vertice.posicion[0]):
            if (actual.padre.posicion[1]!=vertice.posicion[1]):
                vertice.vertice_anterior = actual
                vertice = actual
        actual = actual.padre
    #vertice.vertice_anterior = final
  
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

# Complete the minimumMoves function below.
def minimumMoves(grid, startX, startY, goalX, goalY):
    open = []
    closed = []
    mapa = Mapa(grid,[startX, startY],[goalX, goalY])
    #mapa.imprime_mapa_h()
    mapa.imprimie_extremos()
    #mapa.imprime_coordenadas()
    open.append(mapa.inicio) #Añade el cuadro inicial a la lista abierta.
    camino = False

    while (open)and(not(camino)):
        
        #Busca el cuadro con el coste F más bajo en la lista abierta.
        actual_index = menor_f(open)
        actual = open.pop(actual_index)
        #time.sleep(0.01)
        clear()
        #mapa.introduce_camino(actual)
        #print("giros acumulados: ", actual.giros)
        #mapa.imprime_mapa_recorrido()
        #mapa.reinicar_camino()

        #Cámbialo a la lista cerrada.
        closed.append(actual)

        #Si no es transitable o si está en la lista cerrada, ignóralo.
        vecinos = vecinos_trasitables(mapa, actual, closed)

        for i in vecinos:
            if i == mapa.final:
                camino = True
                i.padre = actual
                i.update()
                break
            
            if not(i in open):
                open.append(i)
                i.padre = actual
                i.update()
                
            elif (i.giros) > (actual.giros):
                i.padre = actual
                i.update()


        
    if camino:
        print("Coordenadas camino: ")
        imprime_coord_camino(mapa.final)
        mapa.imprimie_extremos()
        mapa.introduce_camino(mapa.final)
        print()
        mapa.imprime_mapa_recorrido()
        set_vertices(mapa.final, mapa.inicio)
        print_path_vertices(mapa.final)
        path = get_path_vertices(mapa.final)
        print("giros acumulados: ", mapa.final.giros)
        #return mapa.final.giros
        return len(path)

    return 0


if __name__ == '__main__':
    
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    with open('CastleOnGrid_test_case_0.txt') as file:
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
