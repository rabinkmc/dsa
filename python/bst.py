#    10
#   /  \
#   5    -3
#  / \    \
# 3   2    11
# /\   \
# 3 -2  1
#


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


def tprint(node, inorder=False):
    if node is None:
        return
    if inorder:
        tprint(node.left)
        print(node.val, "->", end="")
        tprint(node.right)
    else:
        print(node.val, "->", end="")
        tprint(node.left)
        tprint(node.right)
