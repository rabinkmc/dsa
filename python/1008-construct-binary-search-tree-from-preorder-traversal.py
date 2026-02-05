# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        inorder = sorted(preorder)
        idx_map = {val: index for index, val in enumerate(inorder)}

        self.pidx = 0

        def dfs(left, right):
            if left > right:
                return None

            root_val = preorder[self.pidx]
            root = TreeNode(root_val)
            self.pidx += 1

            m = idx_map[root_val]
            root.left = dfs(left, m - 1)
            root.right = dfs(m + 1, right)
            return root

        return dfs(0, len(preorder) - 1)
