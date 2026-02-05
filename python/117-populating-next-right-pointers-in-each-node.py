from typing import Optional
from collections import deque


class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def build_tree_level_order(arr, i=0):
    if i >= len(arr) or arr[i] is None:
        return None
    root = Node(arr[i])
    root.left = build_tree_level_order(arr, 2 * i + 1)
    root.right = build_tree_level_order(arr, 2 * i + 2)
    return root


def dfs(node):
    if not node:
        return
    print(node.val, end="->")
    dfs(node.left)
    dfs(node.right)


root = [1, 2, 3, 4, 5, 6, 7]
tree = build_tree_level_order(root)


class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        if not root:
            return None
        q = deque()
        q.append(root)

        while q:
            tmp = []
            count = len(q)
            for _ in range(count):
                node = q.popleft()
                tmp.append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            next = None
            print([x.val for x in tmp])
            for node in tmp[::-1]:
                node.next = next
                next = node
        return root


root = Solution().connect(tree)
