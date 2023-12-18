import math


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(node):
    if node.left:
        dfs(node.left)
    print(node.val)
    if node.right:
        dfs(node.right)


def good_nodes(node, maximum=-math.inf):
    if not node:
        return []
    result = []
    if node.val >= maximum:
        result.append(node)
    return result + good_nodes(node.left, maximum) + good_nodes(node.right, maximum)
