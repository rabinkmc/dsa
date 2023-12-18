# path sum II
from collections import deque


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(node):
    paths = []
    stack = [node]
    path = []
    while stack:
        current = stack.pop()
        path.append(current.val)
        if not current.left and not current.right:
            paths.append(path)
            path = []
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
    print(paths)


seven = Node(7)
two = Node(2)
five = Node(5)
one = Node(1)
eleven = Node(11, left=seven, right=two)
thirteen = Node(13)
four_right = Node(4, left=five, right=one)
four_left = Node(4, left=eleven)
eight = Node(8, left=thirteen, right=four_right)
root = Node(5, left=four_left, right=eight)
dfs(root)
