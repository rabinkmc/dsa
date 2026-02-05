from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 3, 9, 20 , 15, 7
seven = TreeNode(7)
fifteen = TreeNode(15)
twenty = TreeNode(20, left=fifteen, right=seven)
nine = TreeNode(9)
three = TreeNode(3, left=nine, right=twenty)


def pprint(node):
    if not node:
        return
    pprint(node.left)
    print(node.val, end="->")
    pprint(node.right)


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        self.i = n - 1

        idx_map = {inorder[i]: i for i in range(n)}

        def dfs(l, r):
            if l > r:
                return None
            if self.i < 0:
                return None

            root_val = postorder[self.i]
            self.i = self.i - 1
            m = idx_map[root_val]
            print(f"dfs({l}, {r}): {l=}, {m=}, {r=}")
            # right half: m + 1, r
            # left half: l, m - 1
            root = TreeNode(root_val)
            root.right = dfs(m + 1, r)
            root.left = dfs(l, m - 1)
            return root

        return dfs(0, n - 1)


ans = Solution().buildTree(inorder=[9, 3, 15, 20, 7], postorder=[9, 15, 7, 20, 3])
pprint(ans)
