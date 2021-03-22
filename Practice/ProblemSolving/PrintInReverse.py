# https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list-in-reverse/problem

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

def print_singly_linked_list(node, sep):
    while node:
        print(node.data, end='')

        node = node.next

        if node:
            print(sep, end='')

# Complete the reversePrint function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def reversePrint(head):
    node = head
    temp = []
    while node:
        temp.append(node.data)
        node = node.next
    
    for i in reversed(temp):
        print(i)

if __name__ == '__main__':
    
    
    with open('PrintInReverse_1.txt') as file:
        num_test = int(next(file))
        for i_test in range(num_test):
            llist_count = int(next(file))
            llist = SinglyLinkedList()

            for _ in range(llist_count):
                llist_item = int(next(file))
                llist.insert_node(llist_item)

            reversePrint(llist.head)
            print()
