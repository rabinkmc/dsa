stack = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(node):
    if not node:
        return []
    if not node.left and not node.right:
        return [[node.val]]
    lp = [[node.val] + path for path in dfs(node.left)]
    rp = [[node.val] + path for path in dfs(node.right)]
    return lp + rp


# path sum II
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

print(dfs(root))
