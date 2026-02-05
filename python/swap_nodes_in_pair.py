from typing import Optional
def pprint(node):
    if not node:
        return 
    print(node.val, end="->")
    pprint(node.next)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def swap(head):
            if not head or not head.next:
                return head
            b = head.next
            head.next = swap(b.next)
            b.next = head
            return b
        return swap(head)


head = ListNode(
    val=1, 
    next=ListNode(
        val=2,
        next=ListNode(
            val=3,
            next=ListNode(
                val=4
            )
        )
    )
)

ans = Solution().swapPairs(head)
pprint(ans)
