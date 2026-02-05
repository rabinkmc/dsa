class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.val}"


seven = Node(7)
six = Node(6)
five = Node(5)
four = Node(4)
three = Node(3, left=six, right=seven)
two = Node(2, left=four, right=five)
one = Node(1, left=two, right=three)


def dfs(node):
    if not node:
        return
    dfs(node.left)
    dfs(node.right)
    print(node.val, end="->")


dfs(one)
