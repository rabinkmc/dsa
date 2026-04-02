from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


#     1
#   /   \
#  2     3
# / \     \
# 4   5     8
#   / \   /
#  6   12 9

node9 = TreeNode(9)
node6 = TreeNode(6)
node12 = TreeNode(13)
node4 = TreeNode(4)

node8 = TreeNode(8, left=node9)
node5 = TreeNode(5, left=node6, right=node12)
node3 = TreeNode(3, right=node8)
node2 = TreeNode(2, left=node4, right=node5)

root = TreeNode(1, left=node2, right=node3)


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.ans = []

        def dfs(node, curr):
            if not node:
                return
            if not node.left and not node.right:
                if sum(curr) + node.val == targetSum:
                    self.ans.append(curr + [node.val])
                return
            dfs(node.left, curr + [node.val])
            dfs(node.right, curr + [node.val])

        dfs(root, [])
        return self.ans


ans = Solution().pathSum(root, 21)
print(ans)
