class Node:
    def __init__(self, val):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None


def dfs(root):
    if not root:
        return
    print(root.val, end="->")
    dfs(root.left)
    dfs(root.right)


six = Node(6)
one = Node(1)
four = Node(4)
two = Node(2, left=one)
three = Node(3, left=two, right=four)
five = Node(5, left=three, right=six)

six.parent = five
three.parent = five
two.parent = three
four.parent = three
one.parent = two


class Solution:
    def inorderSuccessor(self, node: "Node") -> "Optional[Node]":
        if node.right:
            node = node.right
            while node:
                node = node.left
            return node
        else:
            p = node.parent
            while p and node != parent.left:
                node = p
                p = p.parent
            return p
