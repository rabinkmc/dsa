class TreeNode:
    def __init__(self, x, left=None, right=None, level=0):
        self.val = x
        self.left = left
        self.right = right
        self.parent = None
        self.level = level


six = TreeNode(6)
seven = TreeNode(7)
four = TreeNode(4)
zero = TreeNode(0)
eight = TreeNode(8)
two = TreeNode(2, left=seven, right=four)
five = TreeNode(5, left=six, right=two)
one = TreeNode(1, left=zero, right=eight)
root = TreeNode(3, left=five, right=one)


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        cur = root
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right

            if p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur


print(Solution().lowestCommonAncestor(root, six, two).val)
