from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree_level_order(arr, i=0):
    if i >= len(arr) or arr[i] is None:
        return None
    root = TreeNode(arr[i])
    root.left = build_tree_level_order(arr, 2 * i + 1)
    root.right = build_tree_level_order(arr, 2 * i + 2)
    return root


def dfs(node):
    if not node:
        return
    dfs(node.left)
    print(node.val, end="->")
    dfs(node.right)


root = build_tree_level_order([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def isLeaf(node):
            return not node.left and not node.right

        ans = []

        def dfs(node, total, result):
            if not node:
                return

            if isLeaf(node):
                if total == targetSum:
                    ans.append(result)
                return

            if node.left:
                dfs(node.left, total + node.left.val, result + [node.left.val])

            if node.right:
                dfs(node.right, total + node.right.val, result + [node.right.val])

        if not root:
            return []

        dfs(root, root.val, [root.val])
        return ans


ans = Solution().pathSum(root, 22)
print(ans)
