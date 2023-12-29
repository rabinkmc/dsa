#    10
#   /  \
#   5    -3
#  / \    \
# 3   2    11
# /\   \
# 3 -2  1
#
#
from typing import Optional
from typing import List
from collections import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


three_leaf = TreeNode(3)
minus_two_leaf = TreeNode(-2)
one_leaf = TreeNode(1)
eleven_leaf = TreeNode(11)
three = TreeNode(3, left=three_leaf, right=minus_two_leaf)
two = TreeNode(2, right=one_leaf)
minus_three = TreeNode(-3, right=eleven_leaf)
five = TreeNode(5, left=three, right=two)
root = TreeNode(10, left=five, right=minus_three)


class Solution:
    """
    A height balanced binary tree is a binary tree in which 
    the depth of two subtrees of every node never differs
    by more than one
    """
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if not root:
                return 0
            lh = height(root.left)
            rh = height(root.right)
            if lh == -1 or rh == -1:
                return -1
            if abs(lh - rh) > 1:
                return -1
            return 1 + max(lh, rh)
        return height(root) >= 0

    def iterative(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

ans = Solution().isBalanced(root)
print(ans)
