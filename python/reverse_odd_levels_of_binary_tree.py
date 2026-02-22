from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bfs(root):
    if not root:
        return
    q = deque()
    level = 0
    q.append((root, None))
    while q:
        sz = len(q)
        for _ in range(sz):
            node, parent = q.popleft()
            if not node:
                continue
            if level % 2 == 1:
            if level % 2 == 1:
                parent.left, parent.right = parent.right, parent.left
                q.append((node.right, node))
                q.append((node.left, node))
            else:
                q.append((node.left, node))
                q.append((node.right, node))
        level += 1
    return root


def bfs_print(root):
    if not root:
        return
    q = deque()
    level = 0
    q.append((root, None))
    while q:
        sz = len(q)
        for _ in range(sz):
            node, parent = q.popleft()
            if not node:
                continue
            print(node.val, end="->")
            q.append((node.left, node))
            q.append((node.right, node))
        level += 1
    return root


def build(arr, i):
    if i >= len(arr):
        return None
    root = TreeNode(arr[i])
    root.left = build(arr, 2 * i + 1)
    root.right = build(arr, 2 * i + 2)
    return root


root = [2, 3, 5, 8, 13, 21, 34]
tree = build(root, 0)
bfs(tree)
bfs_print(tree)

# class Solution:
#     def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
