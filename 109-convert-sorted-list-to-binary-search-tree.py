from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


nine = ListNode(9)
five = ListNode(5, nine)
zero = ListNode(0, five)
minusthree = ListNode(-3, zero)
minusten = ListNode(-10, minusthree)


def dfs(node):
    if not node:
        return
    dfs(node.left)
    dfs(node.right)
    print(node.val, end="->")


# class Solution:
#     def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
#         curr = head
#         arr = []
#         while curr:
#             arr.append(curr.val)
#             curr = curr.next
#
#         def bst(arr):
#             if not len(arr):
#                 return None
#             m = len(arr) // 2
#             root = TreeNode(arr[m])
#             root.left = bst(arr[:m])
#             root.right = bst(arr[m + 1 :])
#             return root
#
#         return bst(arr)


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def get_length(node):
            length = 0
            while node:
                length += 1
                node = node.next
            return length

        length = get_length(head)
        self.curr = head

        def bst(l, r):
            if l > r:
                return None
            m = (l + r) // 2
            left = bst(l, m - 1)

            root = TreeNode(self.curr.val)
            self.curr = self.curr.next

            right = bst(m + 1, r)
            root.left = left
            root.right = right
            return root

        return bst(0, length - 1)


root = Solution().sortedListToBST(minusten)
print(dfs(root))
