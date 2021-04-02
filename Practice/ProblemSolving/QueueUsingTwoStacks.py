#https://www.hackerrank.com/challenges/queue-using-two-stacks/problem
'''
A basic queue has the following operations:
Enqueue: add a new element to the end of the queue.
Dequeue: remove the element from the front of the queue and return it.

In this challenge, you must first implement a queue using two stacks. Then process  queries, where each query is one of the following  types:
1 x: Enqueue element  into the end of the queue.
2: Dequeue the element at the front of the queue.
3: Print the element at the front of the queue.
'''
from collections import deque
import os

if __name__ == '__main__':

    q = deque()

    #with open('QueueUsingTwoStacks_Test.txt') as file:
    with open('QueueUsingTwoStacks_Test.txt') as file:
        #n_queries = int(input())
        n_queries = int(next(file))
        for _ in range(n_queries):
            #temp = input().split()
            temp = next(file).split()
            if temp[0] == "1":
                q.append(temp[1])
            elif temp[0] == "2":
                q.popleft()
            elif temp[0] == "3":
                if len(q[0])>0:
                    print(q[0])
                    #file.write(q[0] + '\n')
