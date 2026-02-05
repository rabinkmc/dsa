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


def printdfs(node):
    print(node.val)
    if node.left:
        printdfs(node.left)
    if node.right:
        printdfs(node.right)


count = 0


def dfs(node, targetSum, path=[]):
    global count
    if not node:
        return
    path = path + [node.val]
    cur_sum = 0
    for p in path[::-1]:
        cur_sum += p
        if cur_sum == targetSum:
            count += 1
    dfs(node.left, targetSum, path)
    dfs(node.right, targetSum, path)


def pathSum3(root, targetSum):
    dfs(root, targetSum, 0)


dfs(root, 8)
