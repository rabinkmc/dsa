from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pprint(node):
    if not node:
        return
    pprint(node.left)
    print(node.val)
    pprint(node.right)

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.i = 0
        n = len(preorder)
        idx_map = {}
        for i in range(n):
            idx_map[inorder[i]] = i

        def dfs(left, right):
            if self.i >= n:
                return
            if left > right:
                return
            root_val = preorder[self.i]
            self.i += 1
            m = idx_map[root_val]
            root = TreeNode(val=root_val)
            root.left = dfs(left, m-1)
            root.right = dfs(m+1, right)
            return root
        return dfs(0, n-1)

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

ans = Solution().buildTree(preorder, inorder)
pprint(ans)
