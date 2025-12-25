from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def pprint(node):
    while node:
        print(node.val, end="->")
        node = node.next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oddHead = odd = head
        even = evenHead = head.next
        while even and even.next:
            odd.next = even.next
            odd = even.next
            even.next = odd.next
            even = odd.next
        odd.next = evenHead
        return oddHead
        


seven = ListNode(7)
four = ListNode(4, seven)
six = ListNode(6, four)
five = ListNode(5, six)
three = ListNode(3, five)
one = ListNode(1,three)
two = ListNode(2, one)

pprint(Solution().oddEvenList(two))

