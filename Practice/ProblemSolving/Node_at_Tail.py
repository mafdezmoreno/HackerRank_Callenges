#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

def print_singly_linked_list(node):#,, sep): fptr):
    while node:
        print(str(node.data), end = " ")
        node = node.next
    print()

def insertNodeAtTail(head, valor_insertar):
    
    print("data", valor_insertar)
    if head == None:
        return SinglyLinkedListNode(valor_insertar)
    
    actual = head
    while True:
        
        if actual.next == None:
            actual.next = SinglyLinkedListNode(valor_insertar)
            break
        actual = actual.next
    
    return head


if __name__ == '__main__':
    
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #llist_count = int(input())

    llist = SinglyLinkedList()

    llist_count = 5

    input = [141, 302, 164, 530, 474]

    for i in range(llist_count):
        #llist_item = int(input())
        llist_item = input[i]
        llist_head = insertNodeAtTail(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head)#, ' ') #, fptr)
    #fptr.write('\n')
    #fptr.close()