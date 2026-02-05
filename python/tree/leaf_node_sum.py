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


def tprint(node):
    if node is None:
        return
    print(node.val, "->", end="")
    tprint(node.left)
    tprint(node.right)


def leaf_node_sum(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return root.val
    return leaf_node_sum(root.left) + leaf_node_sum(root.right)


def leaf_node_sum_it(root):
    stack = [root]
    total = 0 
    while stack:
        curr = stack.pop()
        if not curr.left and not curr.right:
            total += curr.val
        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)
    return total

assert leaf_node_sum(root) == 13
assert leaf_node_sum_it(root) == 13
