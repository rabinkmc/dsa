class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


nine = TreeNode(9)
seven = TreeNode(7)
fifteen = TreeNode(15)
twenty = TreeNode(20, left=fifteen, right=seven)
root = TreeNode(3, left=nine, right=twenty)


def dfs_print(node):
    print(node.val)
    if node.left:
        dfs_print(node.left)
    if node.right:
        dfs_print(node.right)


dfs_print(root)
