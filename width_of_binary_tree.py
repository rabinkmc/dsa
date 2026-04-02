from collections import deque


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
#  6   7 9

node9 = TreeNode(9)
node6 = TreeNode(6)
node7 = TreeNode(7)
node4 = TreeNode(4)

node8 = TreeNode(8, left=node9)
node5 = TreeNode(5, left=node6, right=node7)
node3 = TreeNode(3, right=node8)
node2 = TreeNode(2, left=node4, right=node5)

root = TreeNode(1, left=node2, right=node3)


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append(root)
        max_width = 0
        while q:
            sz = len(q)
            width = 0
            for _ in range(sz):
                node = q.popleft()
                width += 1
                if not node:
                    continue
                q.append(node.left)
                q.append(node.right)
            max_width = max(max_width, width)
        return max_width


print(Solution().widthOfBinaryTree(root))
