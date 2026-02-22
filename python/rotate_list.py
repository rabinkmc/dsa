from typing import Optional
from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        n = 0
        tail = head
        n = 1
        while tail.next:
            tail = tail.next
            n += 1
        tail.next = head
        new_tail = head
        for _ in range(n - (k % n) - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        return new_head


l1 = ListNode(
    val=1,
    next=ListNode(
        val=2,
        next=ListNode(val=3, next=ListNode(4, next=ListNode(5, next=ListNode(6)))),
    ),
)


def pprint(node):
    while node:
        print(node.val, end="->")
        node = node.next


ans = Solution().rotateRight(l1, k=2)
pprint(ans)
