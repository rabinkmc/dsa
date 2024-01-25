from typing import Optional
from collections import Counter


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tprint(node, inorder=False):
    if node is None:
        return
    if inorder:
        tprint(node.left)
        print(node.val, "->", end="")
        tprint(node.right)
    else:
        print(node.val, "->", end="")
        tprint(node.left)
        tprint(node.right)


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        self.answer = 0
        def dfs(root, path):
            if not root:
                return
            path = path ^ (1 << root.val)
            if not root.left and not root.right:
                # check if a number is a power of 2
                if path & (path - 1) == 0:
                    self.answer += 1
            dfs(root.left, path)
            dfs(root.right, path)
        dfs(root, 0)
        return self.answer


arr = [2, 3, 1, 3, 1, None, 1]
# arr = [2, 1, 1, 1, 3, None, None, None, None, None, 1]
n = len(arr)


def build(arr, i):
    root = TreeNode(arr[i])
    if 2 * i + 1 < n and arr[2 * i + 1]:
        root.left = build(arr, 2 * i + 1)
    if 2 * i + 2 < n and arr[2 * i + 2]:
        root.right = build(arr, 2 * i + 2)
    return root


root = build(arr, 0)
ans = Solution().pseudoPalindromicPaths(root)
print(ans)
