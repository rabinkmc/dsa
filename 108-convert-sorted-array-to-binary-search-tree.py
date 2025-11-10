from typing import Optional, List
from bst import tprint


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # we know middle element is the root node
        if not len(nums):
            return None

        m = len(nums) // 2
        root = TreeNode(nums[m])
        root.left = self.sortedArrayToBST(nums[:m])
        root.right = self.sortedArrayToBST(nums[m + 1 :])
        return root


nums = [-10, -3, 0, 5, 9]
solution = Solution().sortedArrayToBST(nums)
tprint(solution, inorder=True)
