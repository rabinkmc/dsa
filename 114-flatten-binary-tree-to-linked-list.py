# Definition for a binary tree node.
from typing import List, Optional


def build_tree_level_order(arr, i=0):
    if i >= len(arr) or arr[i] is None:
        return None
    root = TreeNode(arr[i])
    root.left = build_tree_level_order(arr, 2 * i + 1)
    root.right = build_tree_level_order(arr, 2 * i + 2)
    return root


def dfs(node):
    if not node:
        return
    print(node.val, end="->")
    dfs(node.left)
    dfs(node.right)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


tree = build_tree_level_order([1, 2, 5, 3, 4, None, 6])


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        stack = [root]
        prev = None
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            if prev:
                prev.left = None
                prev.right = node
            prev = node


root = Solution().flatten(tree)
print(dfs(root))
