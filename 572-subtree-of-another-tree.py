# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_equal(n1, n2):
            if not n1:
                return not n2
            if not n2:
                return not n1
            return (
                n1.val == n2.val
                and is_equal(n1.left, n2.left)
                and is_equal(n1.right, n2.right)
            )
        def dfs(root, subroot):
            if not root:
                return not subroot
            return (
                is_equal(root, subroot)
                or dfs(root.left, subroot)
                or dfs(root.right, subroot)
            )
        return dfs(root, subroot)
