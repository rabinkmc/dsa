from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def pprint(node):
    while node:
        print(node.val, end='->')
        node = node.next
    print()


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node):
            curr = node
            tail = None
            while curr:
                next_node = curr.next
                curr.next = tail
                tail = curr
                curr = next_node
            return tail
        l1 = reverse(l1)
        l2 = reverse(l2)
        carry = 0

        prev = None
        while l1 or l2 or carry: 
            val1 = 0
            val2 = 0
            if l1:
                val1 = l1.val
            if l2:
                val2 = l2.val
            total = val1 + val2 + carry
            digit = total % 10
            carry = total // 10
            prev = ListNode(digit, prev)
            l1 = l1 and l1.next
            l2 = l2 and l2.next
        return prev

l1 = ListNode(
    val=7,
    next=ListNode(
        val=2,
        next=ListNode(
            val=4, 
            next=ListNode(3)
        )
    )
)
l1 = ListNode(
    val=2,
    next=ListNode(
        val=4,
        next=ListNode(val=3)
    )
)

l2 = ListNode(
    val=5,
    next=ListNode(
        val=6,
        next=ListNode(val=4)
    )
)
l1 = ListNode(val=0)
l2 = ListNode(val=0)
ans = Solution().addTwoNumbers(l1, l2)
pprint(ans)
