from typing import Optional


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        if not root:
            return None
        curr = root
        stack = []
        prev = None
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if prev.val == p.val:
                return curr
            prev = curr
            curr = curr.right
        return None


one = TreeNode(1)
three = TreeNode(3)
root = TreeNode(2, left=one, right=three)
ans = Solution().inorderSuccessor(root, one)
print(ans)
