from collections import defaultdict, deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(list)

        def dfs(node):
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                dfs(node.left)

            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                dfs(node.right)

        dfs(root)
        height = 0
        q = deque()
        q.append(start)
        visited = set()
        while q:
            q_size = len(q)
            for _ in range(q_size):
                node = q.popleft()
                for adj in graph[node]:
                    if adj in visited:
                        continue
                    q.append(adj)
                    visited.add(adj)
            height += 1
        return height - 1


root = TreeNode(
    val=3,
    left=TreeNode(
        val=5,
        left=None,
        right=TreeNode(val=4, left=TreeNode(val=9), right=TreeNode(val=2)),
    ),
    right=TreeNode(val=3, left=TreeNode(10), right=TreeNode(6)),
)

ans = Solution().amountOfTime(root, start=3)
print(ans)
