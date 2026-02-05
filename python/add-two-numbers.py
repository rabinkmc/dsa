from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = prev = ListNode(val=-1, next=None)
        carry = 0
        sum = 0
        while l1 or l2 or carry:
            digit1 = (l1 and l1.val) or 0
            digit2 = (l2 and l2.val) or 0
            sum = digit1 + digit2 + carry
            digit = sum
            if sum >= 10:
                digit = sum - 10
                carry = 1
            else:
                carry = 0
            tmp = ListNode(val=digit)
            prev.next = tmp
            prev = tmp
            l1 = l1 and l1.next
            l2 = l2 and l2.next
        return dummy.next

def pprint(node):
    while node:
        print(node.val, end="->")
        node = node.next

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
ans = Solution().addTwoNumbers(l1, l2)
pprint(ans)
