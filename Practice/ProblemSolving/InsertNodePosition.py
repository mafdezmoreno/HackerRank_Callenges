#https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem

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
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node):
    while node:
        print(node.data)
        node = node.next
            

# Complete the insertNodeAtPosition function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtPosition(head, data, position):
    print(data, position)
    actual = head
    for _ in range(position):
        previo = actual
        actual = actual.next
    previo.next = SinglyLinkedListNode(data)
    previo.next.next = actual
    return head

if __name__ == '__main__':
    
    
    with open('InsertNodePosition_1.txt') as file:
        llist_count = int(next(file))
        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(next(file))
            llist.insert_node(llist_item)

        data = int(next(file))

        position = int(next(file))

    llist_head = insertNodeAtPosition(llist.head, data, position)

    print_singly_linked_list(llist_head)

