from typing import Optional

#    10
#   /  \
#   5    -3
#  / \    \
# 3   2    11
# /\   \
# 3 -2  1
#


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
root = TreeNode(10, left=None, right=minus_three)

"""
main idea: 
learning to use inorder traversal using stack
0. maintain a current
1. keep going left to the current if you can
2. now pop the current element(i.e pop element from stack)
3. process the current element
4. now point the current to its right element and do this again 
   as long as there is a stack or right element
"""
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        prev = float('-inf')
        current = root
        while stack or current:
            # keep going left
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            if prev > current.val:
                return False
            prev = current.val
            current = current.right
        return True

print(Solution().isValidBST(root))
