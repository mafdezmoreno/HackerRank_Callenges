# https://www.hackerrank.com/challenges/castle-on-the-grid/problem?h_r=next-challenge&h_v=zen

# Referencias:
# https://codereview.stackexchange.com/questions/208311/python-a-star-with-fewest-turns-and-shortest-path-variations
import os
from collections import deque
import time
from heapq import heappop, heappush


clear = lambda: os.system('clear')

class Nodo:
    
    posicion = [0, 0]
    giros = 0
    padre = None
    en_recorrido = False

    # Inicialización
    def __init__(self, posicion=[0, 0], final=[0,0]):
        self.posicion = posicion
    
    def update(self):
        self.giros = self.padre.giros

    # Comparadores
    def __lt__(self, other): #<
        return self.giros < other.giros

    def __eq__(self, other): # =
        if(other == None):
            return False
        if(not isinstance(other, Nodo)):
            return False
        return self.giros == other.giros

    # Para que funcione la busqueda en set
    def __hash__(self):
        return hash((self.posicion[0], self.posicion[1]))

    '''
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
    '''
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
                    self.mapa[y][x].en_recorrido = False
    
    def imprime_mapa_recorrido(self):
        for y in range(len(self.mapa)):
            for x in range(len(self.mapa[y])):
                if self.mapa[y][x] == None:
                        print(end="#")
                else:
                    if self.mapa[y][x].posicion == self.inicio.posicion:
                        print(end="I")
                    elif self.mapa[y][x].posicion == self.final.posicion:
                        print(end="F")
                   
                    elif self.mapa[y][x].en_recorrido:
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
            final.en_recorrido = True
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

 
    for i in to_check:
        if (i!=None):
            # para no contar el primer paso como giro
            if curr_pos.posicion == inicio.posicion:
                is_turn = False
            else:   
                
                # movimiento anterior
                if curr_pos.posicion[1] != curr_pos.padre.posicion[1] and curr_pos. posicion[0] == curr_pos.padre.posicion[0]:
                    prev_mov = 'vertical'
                else:
                    prev_mov = 'horizontal'
                
                #movimiento actual
                if curr_pos.posicion[1] != i.posicion[1] and curr_pos.posicion[0] == i.posicion[0]:
                    sig_mov = 'vertical'
                else:
                    sig_mov = 'horizontal'         
                
                # If we're not still moving in the same direction, we have turned.
                is_turn = not (prev_mov == sig_mov)

            vecinos.append((i, is_turn))
            # i:        Nodo vecino
            # is_turn:  Si se ha producido algun grio
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
    
def make_path(mapa: Mapa):
        """Creates list of coordinates representing turns in path.

        :param curr_pos: end point of path.
        :param route: dict of coordinates leading to curr_pos
        :return: tuple containing list of coordinates of turns, len(list of coordinates)
        """
        curvas = []
        x, path_length = 0, 1

        if mapa.final is None:
            print('No hay camino posible')
            return 0

        pos_actual = mapa.final

        while True:
            if  (pos_actual == None) or (pos_actual.padre == None):
                break
            if pos_actual.posicion[x] != pos_actual.padre.posicion[x]:
                if x == 0:
                    x = 1
                else:
                    x = 0
                if pos_actual.posicion != mapa.final.posicion:
                    curvas.append(pos_actual)
                
            pos_actual = pos_actual.padre
            path_length += 1

        print("\n\nVertices: ")
        for i in curvas:
            print(i.posicion, end = " ")
        print("\n")
        return [curvas, path_length]

# Complete the minimumMoves function below.
def iterar(grid, startX, startY, goalX, goalY):

        # Keep track of where we've been.
        visited = set()
        mapa = Mapa(grid,[startX, startY],[goalX, goalY])
        # We'll keep track of the route and the number of turns to reach the curr_pos with a dict.
        # {(position): (turns_count, (previous-position))}
        #rutas = {mapa.inicio: None}

        # turn_count is used to promote routes with fewer turns.
        # turn_count = {mapa.inicio: 0} # Diccionario: indice es el nodo
                                      # valor el número de giros
        open_pos = []
        heappush(open_pos, (mapa.inicio.giros, mapa.inicio))
        terminar = False
        giros_acumulados = 0
        while (len(open_pos)>0) and not(terminar):
            
            # priority queue: Los nodos con menos giros acumulados están al inicio
            giros_acumulados, pos_actual = heappop(open_pos)
            
            #if pos_actual in visited:
            #    continue
            time.sleep(0.5)
            clear()
            mapa.introduce_camino(pos_actual)
            mapa.imprime_mapa_recorrido()
            mapa.reinicar_camino()
            print(giros_acumulados, pos_actual.posicion)

            #prev = route[curr_pos]  # Always remember where you came from so we know if we've turned.
            visited.add(pos_actual)  # But keep moving forward. Never go back!

            neighbors_list = vecinos_trasitables(mapa, pos_actual, mapa.inicio)
            for vecino, did_turn in neighbors_list:
                if  vecino in visited:
                    continue

                if vecino.padre!= None:
                    # Si ya ha estado antes, se actualiza el numero de giros con los que contiene la ruta mas corta
                    vecino.giros = min(vecino.padre.giros, giros_acumulados + int(did_turn))
                #else:
                    vecino.giros = giros_acumulados + int(did_turn)
                #print(vecino.posicion, vecino.giros)
                # In any case add this place to the list of places to explore.
                heappush(open_pos, (vecino.giros, vecino))

                # Comprobar caminos más cortos
                old_ruta = vecino.padre
                # If so, does the old_route take more turns than the current route to get to pos?
                if old_ruta:
                    if old_ruta.giros < vecino.padre.giros:
                        # Si se alcanza en menos giros:
                        vecino.padre = pos_actual
                else:
                    vecino.padre = pos_actual

            for i in neighbors_list:
                if i[0].posicion == mapa.final.posicion:
                    terminar = True

        # Wait until open_pos is exhausted to ensure a shorter path doesn't end our search prematurely.
        print("\nGiros acumulados: ", giros_acumulados)
        resultado = make_path(mapa)
        print("Giros: \t\t", len(resultado[0]))
        print("Movimientos: \t", len(resultado[0])+1)
        print("Longitud: \t", resultado[1])

        mapa.introduce_camino(pos_actual)
        mapa.imprime_mapa_recorrido()
        mapa.reinicar_camino()
    
        return len(resultado[0])+1

# Complete the minimumMoves function below.
def minimumMoves(grid, startX, startY, goalX, goalY):
    
    a_b = iterar(grid, startX, startY, goalX, goalY)
    #time.sleep(1)
    #b_a = iterar(grid, goalX, goalY, startX, startY)
    #return min(a_b, b_a)
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

        result = minimumMoves(grid, startY, startX, goalY, goalX,)

        print("\nResultado: ")
        print(" \t \t", end = " ")
        print(result, "\n")

    #fptr.write(str(result) + '\n')
    #fptr.close()
