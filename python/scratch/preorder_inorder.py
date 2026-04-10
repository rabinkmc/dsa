from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx_map = {val: i for i, val in enumerate(inorder)}
        self.idx = 0
        n = len(preorder)

        def build(l, r):
            if self.idx == n:
                return None
            if l > r:
                return None
            val = preorder[self.idx]
            m = idx_map[val]
            root = TreeNode(val)
            self.idx += 1
            root.left = build(l, m - 1)
            root.right = build(m + 1, r)
            return root

        return build(0, len(preorder) - 1)


inorder = [9, 3, 15, 20, 7]
preorder = [3, 9, 20, 15, 7]
ans = Solution().buildTree(preorder, inorder)
print(ans)
