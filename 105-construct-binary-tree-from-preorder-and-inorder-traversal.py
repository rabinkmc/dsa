class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_map = {}
        for i, val in enumerate(inorder):
            index_map[val] = i
        if not preorder or not inorder:
            return None
        root_val = preorder[0]
        m = index_map[root_val]
        root = TreeNode(root_val)
        root.left = self.buildTree(preorder[1 : m + 1], inorder[:m])
        root.right = self.buildTree(preorder[m + 1 :], inorder[m + 1 :])
        return root
