class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        one thing to remember, depth of a tree is the number of nodes along the longest path from the root node down to the farthest leaf node.
        while height of a tree is the longest path from root to the farthest leaf 
        """
        if not root:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
