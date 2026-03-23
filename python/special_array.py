from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append(root)
        level = 0
        while queue:
            sz = len(queue)
            curr = []
            prev = -1
            for _ in range(sz):
                node = queue.popleft()
                if level % 2 == 0:
                    if node.val % 2 == 0:
                        return False
                    if prev != -1 and node.val <= prev:
                        return False
                else:
                    if node.val % 2 == 1:
                        return False
                    if prev != -1 and node.val >= prev:
                        return False
                prev = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return True


root = TreeNode(
    1,
    TreeNode(10, TreeNode(3, TreeNode(12), TreeNode(8)), None),
    TreeNode(4, TreeNode(7, TreeNode(6), None), TreeNode(9, None, TreeNode(2))),
)
ans = Solution().isEvenOddTree(root)
print(ans)
