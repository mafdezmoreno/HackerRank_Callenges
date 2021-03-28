# https://www.hackerrank.com/challenges/swap-Nodos-algo/problem?h_r=next-challenge&h_v=zen

import itertools

class Nodo:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None
        self.level = None

class BinarySearchTree:
    def __init__(self): 
        self.root = Nodo(1)
        self.root.level = 1

    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.info)
            res = res + self.inorderTraversal(root.right)
        return res
    
# Utility function to print the two-dimensional view of a binary tree using
# reverse inorder traversal
def printBinaryTree(root, space, height):
 
    # Base case
    if root is None:
        return
 
    # increase distance between levels
    space += height
 
    # print right child first
    printBinaryTree(root.right, space, height)
    print()
 
    # print the current node after padding with spaces
    for i in range(height, space):
        print(' ', end='')
 
    print(root.info, end='')
 
    # print left child
    print()
    printBinaryTree(root.left, space, height)


def crea_arbol(indexes):
    arbol = BinarySearchTree()
    cola = list()
    cola.insert(0,arbol.root)
    for i in indexes:
        actual = cola.pop()
        if (i[0]!=-1):
            actual.left = Nodo(i[0])
            actual.left.level = actual.level+1
            cola.insert(0, actual.left)
        if (i[1]!=-1):
            actual.right = Nodo(i[1])
            actual.right.level = actual.level+1
            cola.insert(0, actual.right)    
    return arbol

def Nodos_at_level(nodo, level):
    list_Nodos = list()
    def repetir(nodo, list_Nodos, level):
        if nodo.left:
            list_Nodos = repetir(nodo.left, list_Nodos, level)
        if nodo.level == level:
            list_Nodos.append(nodo)
        if nodo.right:
            list_Nodos = repetir(nodo.right, list_Nodos, level) 
        return list_Nodos
    list_Nodos = repetir(nodo, list_Nodos, level)
    return list_Nodos

def swapNodos(indexes, queries):

    to_return = []
    arbol = crea_arbol(indexes)
    printBinaryTree(arbol.root, 0, 3)
    to_swap = []
    temp = []
    for i in range(len(queries)):
        prev_level = -1
        for x in queries[i:]:
            if prev_level == x:
                continue
            temp.append(Nodos_at_level(arbol.root, x))
            prev_level = x
        to_swap.append(list(itertools.chain.from_iterable(temp)))
        temp.clear()
    
    print( "=====")
    for x in to_swap:
        for i in x:
            print (i.info, end= " ")
        print()
    print( "=====")

    for lista in to_swap:
        for nodo in lista:
            temp = nodo.left
            nodo.left = nodo.right
            nodo.right = temp
        to_return.append(arbol.inorderTraversal(arbol.root))
        printBinaryTree(arbol.root, 0, 3)
        print("=================")
    return to_return

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

        result = swapNodos(indexes, queries)

        for i in result:
            print (i)

        # Expected result for test case 0
        print("Expected result for test case 0")
        print([14, 8, 5, 9, 2, 4, 13, 7, 12, 1, 3, 10, 15, 6, 17, 11, 16])
        print([9, 5, 14, 8, 2, 13, 7, 12, 4, 1, 3, 17, 11, 16, 6, 10, 15])