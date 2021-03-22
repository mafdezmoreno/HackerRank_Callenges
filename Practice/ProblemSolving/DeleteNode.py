# https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list/problem

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

# Complete the deleteNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def deleteNode(head, position):
    
    if position == 0:
        return head.next

    actual = head
    
    for _ in range(position-1):
        actual = actual.next
    
    if (actual.next)and(actual.next.next):
        if (actual):
            actual.next = actual.next.next
    else:
        actual.next = None

    return head

if __name__ == '__main__':
    
    
    with open('DeleteNode_2.txt') as file:
        llist_count = int(next(file))
        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(next(file))
            llist.insert_node(llist_item)

        position = int(next(file))

    llist_head = deleteNode(llist.head, position)

    print_singly_linked_list(llist_head)