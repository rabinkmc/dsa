from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lte(arr, target):
    l = 0
    r = len(arr) - 1
    ans = -1
    while l <= r:
        m = l + (r - l) // 2
        if arr[m] <= target:
            ans = arr[m]
            l = m + 1
        else:
            r = m - 1
    return ans


def gte(arr, target):
    l = 0
    r = len(arr) - 1
    ans = -1
    while l <= r:
        m = l + (r - l) // 2
        if arr[m] >= target:
            ans = arr[m]
            r = m - 1
        else:
            l = m + 1
    return ans


class Solution:
    def closestNodes(
        self, root: Optional[TreeNode], queries: List[int]
    ) -> List[List[int]]:
        out = []
        arr = []

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            arr.append(root.val)
            dfs(root.right)

        dfs(root)
        for target in queries:
            lt = lte(arr, target)
            gt = gte(arr, target)
            out.append([lt, gt])
        return out


root = TreeNode(
    6,
    left=TreeNode(2, left=TreeNode(1), right=TreeNode(4)),
    right=TreeNode(13, left=TreeNode(9), right=TreeNode(15, left=TreeNode(14))),
)

queries = [2, 5, 16]
ans = Solution().closestNodes(root, queries)
print(ans)
