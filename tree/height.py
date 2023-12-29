#    10
#   /  \
#   5    -3
#  / \    \
# 3   2    11
# /\   \
# 3 -2  1
#
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


three_leaf = TreeNode(3)
minus_two_leaf = TreeNode(-2)
one_leaf = TreeNode(1)
eleven_leaf = TreeNode(11)
three = TreeNode(3, left=three_leaf, right=minus_two_leaf)
two = TreeNode(2, right=one_leaf)
minus_three = TreeNode(-3, right=eleven_leaf)
five = TreeNode(5, left=three, right=two)
root = TreeNode(10, left=five, right=minus_three)


def tprint(node):
    if node is None:
        return
    print(node.val, "->", end="")
    tprint(node.left)
    tprint(node.right)


def rec_height(node):
    if not node:
        return -1

    lh = rec_height(node.left)
    rh = rec_height(node.right)
    return 1 + max(lh, rh)


def it_height(node: TreeNode):
    queue = deque([(node, 0)])
    ans = 0
    while queue:
        curr, level = queue.popleft()
        ans = max(ans, level)
        if curr.left:
            queue.append((curr.left, level + 1))
        if curr.right:
            queue.append((curr.right, level + 1))
    return ans


h = rec_height(root)
ith = it_height(root)
print(h, ith)
