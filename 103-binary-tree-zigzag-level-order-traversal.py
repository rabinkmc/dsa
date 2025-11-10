from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


seven = TreeNode(7)
fifteen = TreeNode(15)
twenty = TreeNode(20, fifteen, seven)
nine = TreeNode(9)
three = TreeNode(3, nine, twenty)

five = TreeNode(5)
four = TreeNode(4)
three = TreeNode(3, left=None, right=five)
two = TreeNode(2, left=four, right=None)
one = TreeNode(1, left=two, right=three)


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        q = deque()
        level = 0
        q.append(root)
        while q:
            count = len(q)
            tmp = []
            for _ in range(count):
                node = q.popleft()
                tmp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if level % 2 == 1:
                tmp = tmp[::-1]
            result.append(tmp)

            level += 1
        return result


print(Solution().zigzagLevelOrder(one))
