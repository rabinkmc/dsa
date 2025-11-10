from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def build_tree_level_order(arr, i=0):
    if i >= len(arr) or arr[i] == "#":
        return None
    root = TreeNode(arr[i])
    root.left = build_tree_level_order(arr, 2 * i + 1)
    root.right = build_tree_level_order(arr, 2 * i + 2)
    return root


def dfs(root):
    if not root:
        return
    print(root.val, end="->")
    dfs(root.left)
    dfs(root.right)


class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string."""
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if not node:
                continue
            res.append(str(node.val))
            stack.append(node.right)
            stack.append(node.left)
        return ",".join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        arr = [int(x) for x in data.split(",")]
        low = -float("inf")
        high = float("inf")
        self.idx = 0
        print(arr)

        def dfs(low, high):
            if self.idx == len(arr):
                return None
            val = arr[self.idx]
            if val < low or val > high:
                return None
            self.idx += 1
            root = TreeNode(val)
            root.left = dfs(low, val)
            root.right = dfs(val, high)
            return root

        return dfs(low, high)


root = build_tree_level_order([3, 1, 4, None, 2])
root = Codec().deserialize("3,1,4,2")
print(dfs(root))
