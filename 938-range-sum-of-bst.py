# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

eighteen = TreeNode(18)
fifteen = TreeNode(15, right=eighteen)
ten = TreeNode(10, right=fifteen)
three = TreeNode(3)
seven = TreeNode(7)
five = TreeNode(5, left=3, right=seven)

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.answer = 0
        def traverse(node):
            if node.left:
                traverse(node.left, ans)
            if low <= node.val <= high:
                self.answer += node.val
            if node.right:
                traverse(node.right, ans)
        traverse(node)
