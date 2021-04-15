#https://www.hackerrank.com/challenges/compare-two-linked-lists/problem?isFullScreen=true
#!/bin/python3

import os
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

class Nodo():
    
    hijo = None
    valor = -1
    n_hijos = 0

    def __init__(self, valor = None) -> None:
        self.valor = valor
        pass

class SinglyLinkedList():
    
    cola = None
    head = None

    def insert_node(self, valor) -> None:
        
        if self.head == None:
            self.head = Nodo(valor)
            self.cola = self.head
        else:
            temp = Nodo(valor)
            self.cola.hijo = temp
            self.cola = temp
            self.head.n_hijos +=1
            hijos = self.head.n_hijos
            nodo = self.head.hijo
            while nodo != None:
                hijos -= 1
                nodo.n_hijos = hijos
                nodo = nodo.hijo
        pass
    
    def imprime(self):
        nodo = self.inicio
        while nodo != None:
            print(nodo.valor, ": ", nodo.n_hijos, end = " | ")
            nodo = nodo.hijo
        print()

def compare_lists(llist1, llist2):
    
    while True:
        if (llist1 == None) and (llist2 == None):
            return 1
        elif (llist1 == None) or (llist2 == None):
            return 0
        elif (llist1.valor == llist2.valor):
            print(llist1.valor, llist2.valor)
            llist1 = llist1.hijo
            llist2 = llist2.hijo 
        else:
            return 0
    return 1



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        result = compare_lists(llist1.head, llist2.head)

        fptr.write(str(int(result)) + '\n')

    fptr.close()