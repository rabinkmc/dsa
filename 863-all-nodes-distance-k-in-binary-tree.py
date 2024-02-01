# Definition for a binary tree node.
from typing import List
from collections import defaultdict, deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build(arr, i):
    n = len(arr)
    root = TreeNode(arr[i])
    if 2 * i + 1 < n and arr[2 * i + 1]:
        root.left = build(arr, 2 * i + 1)
    if 2 * i + 2 < n and arr[2 * i + 2]:
        root.right = build(arr, 2 * i + 2)
    return root


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)

        def dfs(root, parent=None):
            if not root:
                return
            if parent:
                graph[parent.val].append(root.val)
                graph[root.val].append(parent.val)
            dfs(root.left, root)
            dfs(root.right, root)

        dfs(root, None)
        queue = [target.val]
        visited = {target.val}
        for _ in range(k):
            temp = []
            for node in queue:
                for next_node in graph[node]:
                    if next_node not in visited:
                        temp.append(next_node)
                        visited.add(next_node)
            queue = temp
        return queue


arr = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
root = build(arr, 0)
ans = Solution().distanceK(root, root.left, 2)
print(ans)
