
# https://www.hackerrank.com/challenges/swap-Nodos-algo/problem?h_r=next-challenge&h_v=zen

from functools import total_ordering
import itertools
from collections import deque

class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None
        self.level = None

class BinarySearchTree:
    def __init__(self): 
        self.root = Node(1)
        self.root.level = 1

    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.info)
            res = res + self.inorderTraversal(root.right)
        return res
    
# impresion sencilla del arbol binario. Para depuración
def imprime_arbol(raiz, separacion, altura):
 
    if raiz is None:
        return
 
    # increase distance between levels
    separacion += altura
 
    # derecho
    imprime_arbol(raiz.right, separacion, altura)
    print()
 
    # imprime nodo
    for i in range(altura, separacion):
        print(' ', end='')
 
    print(raiz.info, end='')
 
    # izquierdo
    print()
    imprime_arbol(raiz.left, separacion, altura)


def crea_arbol(indexes):
    arbol = BinarySearchTree()
    cola = list()
    cola.insert(0,arbol.root)
    for i in indexes:
        actual = cola.pop()
        if (i[0]!=-1):
            actual.left = Node(i[0])
            actual.left.level = actual.level+1
            cola.insert(0, actual.left)
        if (i[1]!=-1):
            actual.right = Node(i[1])
            actual.right.level = actual.level+1
            cola.insert(0, actual.right)    
    return arbol

def swapNodos(indexes, queries, N):

    to_return = []
    arbol = crea_arbol(indexes)
    #imprime_arbol(arbol.root, 0, 3)
    root = arbol.root
    for i in range(len(queries)):
        swap(root, queries[i])
        to_return.append(in_order_traverse(root))
        #imprime_arbol(arbol.root, 0, 3)
        #print('')
    
    #for i in to_return:
    #    print(i)

    return to_return

def in_order_traverse(root):

    cola = deque([root])
    visitados = set()
    to_return = []
    while cola:
        node = cola.pop()
        if node is None:
            continue
        if node.info in visitados:
            #print(node.info, end=' ')
            to_return.append(node.info)
            continue
        visitados.add(node.info)
        cola.append(node.right)
        cola.append(node)
        cola.append(node.left)
    #print(to_return)
    return to_return
    
def swap(root, k):
    q = deque([(root, 1)])
    while q:
        node, level = q.popleft()
        if node is None:
            continue
        if level % k == 0:
            node.left, node.right = node.right, node.left
        q.append((node.left, level+1))
        q.append((node.right, level+1))


if __name__ == '__main__':

    with open('SwapNodes_Test_1.txt') as file:
        
        n = int(next(file))

        indexes = []
        for _ in range(n):
            indexes.append(list(map(int, next(file).split())))

        queries_count = int((next(file)))

        queries = []

        for _ in range(queries_count):
            queries_item = int((next(file)))
            queries.append(queries_item)

        resultado = swapNodos(indexes, queries, n)

        for i in resultado:
            print (i)

        # Expected result for test case 0
        print("Expected result for test case 0")
        print([14, 8, 5, 9, 2, 4, 13, 7, 12, 1, 3, 10, 15, 6, 17, 11, 16])
        print([9, 5, 14, 8, 2, 13, 7, 12, 4, 1, 3, 17, 11, 16, 6, 10, 15])