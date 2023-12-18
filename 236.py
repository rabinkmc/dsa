# Definition for a binary tree node.


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
        def dfs(node, parent=None, level=0):
            if not node:
                return node
            node.parent = parent
            node.level = level
            dfs(node.left, node, level + 1)
            dfs(node.right, node, level + 1)

        dfs(root)

        pnode = p
        qnode = q
        while pnode and qnode and pnode.level > qnode.level:
            pnode = pnode.parent
        while qnode and qnode.level > pnode.level:
            qnode = qnode.parent

        while pnode and qnode:
            if pnode == qnode:
                return pnode
            pnode = pnode.parent
            qnode = qnode.parent

        return root


print(Solution().lowestCommonAncestor(root, six, two).val)
