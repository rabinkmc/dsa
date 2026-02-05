## path sum 3
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.output = 0

        def helper(node):
        def dfs(node, target):
            if not node:
                return 0
            dfs(node.left, target)
            dfs(node.right, target)

        dfs(root, target=targetSum)


seven = TreeNode(7)
two = TreeNode(2)
five = TreeNode(5)
one = TreeNode(1)
eleven = TreeNode(11, left=seven, right=two)
thirteen = TreeNode(13)
four_right = TreeNode(4, left=five, right=one)
four_left = TreeNode(4, left=eleven)
eight = TreeNode(8, left=thirteen, right=four_right)
root = TreeNode(5, left=four_left, right=eight)


print(Solution().pathSum(root, 9))
