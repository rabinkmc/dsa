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


def inorder_i(node):
    stack = []
    res = []
    curr = node
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        res.append(curr.val)
        curr = curr.right
    return res


def preorder_i(node):
    stack = [node]
    res = []
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res


def postorder_i(node):
    stack = [node]
    res = []
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return res[::-1]


def levelorder_i(node):
    if not node:
        return []
    q = deque([node])
    res = []
    while q:
        sz = len(q)
        curr = []
        for _ in range(sz):
            node = q.popleft()
            curr.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(curr)
    return res


def rhs_view(node):
    if not node:
        return []
    q = deque([node])
    res = []
    while q:
        sz = len(q)
        curr = None
        for _ in range(sz):
            node = q.popleft()
            curr = node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(curr)
    return res


print(levelorder_i(root))
