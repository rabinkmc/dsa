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


def max_depth(node):
    if not node:
        return 0
    lh = max_depth(node.left)
    rh = max_depth(node.right)
    return max(lh, rh) + 1
