from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    #     index_map = {}
    #     for i, val in enumerate(inorder):
    #         index_map[val] = i
    #     if not preorder or not inorder:
    #         return None
    #     root_val = preorder[0]
    #     m = index_map[root_val]
    #     root = TreeNode(root_val)
    #     root.left = self.buildTree(preorder[1 : m + 1], inorder[:m])
    #     root.right = self.buildTree(preorder[m + 1 :], inorder[m + 1 :])
    #     return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_map = {}
        for i, val in enumerate(inorder):
            index_map[val] = i

        self.idx = 0
        n = len(preorder)

        def dfs(l, r):
            if l > r:
                return None

            if self.idx == n:
                return None

            root_val = preorder[self.idx]
            m = index_map[root_val]

            root = TreeNode(root_val)
            self.idx += 1

            root.left = dfs(l, m)
            root.right = dfs(m + 1, r)
            return root

        return dfs(0, n - 1)


seven = TreeNode(7)
six = TreeNode(6)
five = TreeNode(5)
four = TreeNode(4)
three = TreeNode(3, left=six, right=seven)
two = TreeNode(2, left=four, right=five)
one = TreeNode(1, left=two, right=three)

preorder = [1, 2, 4, 5, 3, 6, 7]
inorder = [4, 2, 5, 1, 6, 3, 7]


def dfs(node):
    if not node:
        return
    print(node.val)
    dfs(node.left)
    dfs(node.right)


dfs(Solution().buildTree(preorder, inorder))
