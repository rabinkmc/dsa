class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def pprint(node):
    if not node:
        return 
    print(node.val)
    pprint(node.left)
    pprint(node.right)

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root
        while node:
            if p.val < node.val and q.val < node.val:
                node = node.left
            elif p.val > node.val and q.val > node.val:
                node = node.right
            else:
                return node
