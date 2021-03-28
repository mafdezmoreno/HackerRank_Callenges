#https://programs.programmingoneonone.com/2021/03/hackerrank-swap-nodes-algo-solution.html

from collections import deque
from types import new_class

class Node:
    def __init__(self, index):
        self.left = None
        self.right = None
        self.index = index

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
    
def in_order_traverse(root):
    """Don't use recursion b/c of recursion limit."""
    stack = deque([root])
    visited = set()
    while stack:
        node = stack.pop()
        if node is None:
            continue
        if node.index in visited:
            print(node.index, end=' ')
            continue
        visited.add(node.index)
        stack.append(node.right)
        stack.append(node)
        stack.append(node.left)

def swap(root, k):
    """Don't use recursion b/c of recursion limit."""
    q = deque([(root, 1)])
    while q:
        node, level = q.popleft()
        if node is None:
            continue
        if level % k == 0:
            node.left, node.right = node.right, node.left
        q.append((node.left, level+1))
        q.append((node.right, level+1))

with open('SwapNodes_Test_1.txt') as file:

    # get number of nodes    
    N = int(next(file))

    # create node list
    nodes = [None]*(N+1)
    for i in range(1, N+1):
        n = Node(i)
        n.left_index, n.right_index = [v if v > 0 else 0 for v in map(int, next(file).split())]
        nodes[i] = n

    # fill out node objects
    for n in nodes[1:]:
        left = nodes[n.left_index]
        right = nodes[n.right_index]
        n.left = left
        n.right = right

    T = int(next(file))
    root = nodes[1]
    # do the swapping
    for _ in range(T):
        k = int(next(file))
        swap(root, k)
        in_order_traverse(root)
        print('')

# Expected result for test case 0
print("Expected result for test case 0")
print([14, 8, 5, 9, 2, 4, 13, 7, 12, 1, 3, 10, 15, 6, 17, 11, 16])
print([9, 5, 14, 8, 2, 13, 7, 12, 4, 1, 3, 17, 11, 16, 6, 10, 15])