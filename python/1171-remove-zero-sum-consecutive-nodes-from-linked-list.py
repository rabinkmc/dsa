# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val}->{self.next}"

    def __repr__(self):
        return f"{self.val}->{self.next}"

def build_list(arr):
    prev = None
    n = len(arr)
    for i in range(n - 1, -1, -1):
        prev = ListNode(val=arr[i], next=prev)
    return prev

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        psum = [0]
        curr = head
        res = []
        while curr:
            current_sum = curr.val + psum[-1]
            if current_sum in psum:
                while psum[-1] != current_sum:
                    psum.pop()
                    res.pop()
            else:
                res.append(curr.val)
                psum.append(current_sum)
            curr = curr.next
        return build_list(res)



arr = [1,2,-3,3,1]
head = build_list(arr)
ans = Solution().removeZeroSumSublists(head)
print(ans)

