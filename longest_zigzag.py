# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(10)
root_left = TreeNode(5)

three_leaf = TreeNode(3)
minus_two_leaf = TreeNode(-2)
one_leaf = TreeNode(1)
eleven_leaf = TreeNode(11)
three = TreeNode(3, left=three_leaf, right=minus_two_leaf)
two = TreeNode(2, right=one_leaf)
minus_three = TreeNode(-3, right=eleven_leaf)
five = TreeNode(5, left=three, right=two)
root = TreeNode(10, left=five, right=minus_three)


def dfs(node):
    stack = [(node, 0, "")]
    ans = 0
    while stack:
        current, depth, dd = stack.pop()
        ans = max(depth, ans)
        if current.left:
            depth = depth + 1 if dd != "l" else 1
            stack.append((current.left, depth, "l"))
        if current.right:
            depth = depth + 1 if dd != "r" else 1
            stack.append((current.right, depth, "r"))

    return ans


print(dfs(root))
