from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(node):
    if not node:
        return
    dfs(node.left)
    dfs(node.right)
    print(node.val, end="->")


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        index_map = {}
        for i, val in enumerate(inorder):
            index_map[val] = i

        def dfs(inorder, postorder):
            if not postorder or not inorder:
                return None
            root_val = postorder[-1]
            m = index_map[root_val]
            root = TreeNode(root_val)
            root.right = self.buildTree(inorder[m + 1 :], postorder[m:-1])
            root.left = self.buildTree(inorder[:m], postorder[:m])
            return root

        return dfs(inorder, postorder)


inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
root = Solution().buildTree(inorder, postorder)
print(dfs(root))
