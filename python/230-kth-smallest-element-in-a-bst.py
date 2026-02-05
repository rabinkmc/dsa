# Definition for a binary tree node.
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


root = build_tree_level_order([3, 1, 4, None, 2])
k = 1


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        i = 0
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            i += 1
            if i == k:
                return curr.val
            curr = curr.right
        return -1


ans = Solution().kthSmallest(root, 5)
print(ans)
