from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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


root = build_tree_level_order([1, 2, 3])


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = 0
        stack = [(root, root.val)]
        while stack:
            node, csum = stack.pop()
            if not node.left and not node.right:
                ans += csum
            if node.left:
                stack.append((node.left, csum * 10 + node.left.val))
            if node.right:
                stack.append((node.right, csum * 10 + node.right.val))

        return ans


print(Solution().sumNumbers(root))
