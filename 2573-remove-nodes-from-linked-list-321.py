# https://leetcode.com/contest/weekly-contest-321/problems/remove-nodes-from-linked-list/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val}->{self.next}"



from typing import Optional


def build_list(arr):
    prev = None
    n = len(arr)
    for i in range(n - 1, -1, -1):
        prev = ListNode(val=arr[i], next=prev)
    return prev

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        curr = head
        while curr:
            while stack and stack[-1] < curr.val:
                stack.pop()
            stack.append(curr.val)
            curr = curr.next
        return build_list(stack)



head = build_list([5, 2, 13, 3, 8])
print(head)


print(Solution().removeNodes(head))
