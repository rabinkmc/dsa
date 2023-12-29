#    1 0
#   /  \
#   5    -3
#  / \    \
# 3   2    11
# /\   \
# 3 -2  1
#
from typing import Optional


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


def tprint(node):
    if node is None:
        return
    print(node.val, "->", end="")
    tprint(node.left)
    tprint(node.right)

class Solution:
    def dfs(self, root: Optional[TreeNode]):
        # diameter and depth
        if not root:
            return (0, 0) 
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        diameter = max(left[0], right[0], left[1] + right[1])
        depth = 1 + max(left[1], right[1])
        return diameter, depth


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)[0] 

ans = Solution().diameterOfBinaryTree(root)
print(ans)
