#!/bin/python3
# https://www.hackerrank.com/challenges/insert-a-node-at-the-head-of-a-linked-list/problem?h_r=next-challenge&h_v=zen&isFullScreen=true

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

def print_singly_linked_list(node):#, sep, fptr):
    while node:
        #fptr.write(str(node.data))
        print(node.data)
        node = node.next
        #if node:
        #    fptr.write(sep)

def insertNodeAtHead(llist, data):

    if llist == None:
        llist = SinglyLinkedListNode(data)
        return llist
    temp = llist
    llist = SinglyLinkedListNode(data)
    llist.next = temp
    return llist

if __name__ == '__main__':

    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #llist_count = int(input())
    llist_count = 5
    input = [383, 484, 392, 975, 321]
    llist = SinglyLinkedList()

    for i in range(llist_count):
        #llist_item = int(input())
        llist_item = input[i]
        llist_head = insertNodeAtHead(llist.head, llist_item)
        llist.head = llist_head
    
    print_singly_linked_list(llist.head)
    #print_singly_linked_list(llist.head, '\n', fptr)
    #fptr.write('\n')
    #fptr.close()