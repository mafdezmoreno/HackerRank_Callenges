# https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list/problem?isFullScreen=true
# Complete the printLinkedList function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

class Node: 

	def __init__(self, data): 
		self.data = data
		self.next = None

class SinglyLinkedList: 
    
    def __init__(self): 
        self.head = None
        self.tail = None
    
    def insert_node(self, next_data):
        if (self.head):
            self.tail.next = Node(next_data)
            self.tail = self.tail.next
        else:
            self.head =  Node(next_data)
            self.tail = self.head

def printLinkedList(head):

    temp = head
    while (temp):
        print (temp.data, end = " ")
        temp = temp.next
    print()

if __name__ == '__main__':
    #llist_count = int(input())
    llist_count = 2
    llist = SinglyLinkedList()
    datos = [16, 13, 12, 11, 10, 9, 8, 7, 6, 0]
    #for _ in range(llist_count):
    #    llist_item = int(input())
    #    llist.insert_node(llist_item)
    
    for i in datos:
        llist.insert_node(i)

    printLinkedList(llist.head)