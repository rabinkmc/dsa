class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build(arr, i):
    n = len(arr)
    root = TreeNode(arr[i])
    if 2*i + 1 < n and arr[2*i+1]:
        root.left = build(arr, 2*i + 1)
    if 2*i + 2 < n and arr[2*i+2]:
        root.right = build(arr, 2*i + 2)
    return root
