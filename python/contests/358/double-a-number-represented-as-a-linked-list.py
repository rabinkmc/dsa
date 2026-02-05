from typing import List, Optional


"""
                      1   1
curr = 1->8->9  - 9 - 8 - 1
curr = 1->8->9  - 9 - 8 - 1
sum = 3-7-8     - 8 - 7 - 3
"""

def reverse(head):
    curr = head
    prev = None
    # prev => curr

    while curr:
        # cur -> next-node
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

nine_3 = ListNode(9)
nine_2 = ListNode(9, next=nine_3)
nine_1= ListNode(9, next=nine_2)


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = reverse(head)
        carry = 0
        ans = None
        while curr:
            _sum = 2*curr.val + carry
            val = _sum % 10 
            carry = _sum // 10
            ans = ListNode(val, next=ans)
            curr = curr.next
        if carry: 
            return ListNode(1, next=ans)
        return ans


ans = Solution().doubleIt(nine_1)
print(ans.next.next.next.val)
