from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(l, r):
            if l > r:
                return None
            m = l + (r - l) // 2
            root = TreeNode(nums[m])
            root.left = build(l, m - 1)
            root.right = build(m + 1, r)
            return root

        return build(0, len(nums) - 1)


def pprint(node):
    if not node:
        return
    print(node.val, end="->")
    pprint(node.left)
    pprint(node.right)


ans = Solution().sortedArrayToBST(nums=[1, 3])
pprint(ans)
