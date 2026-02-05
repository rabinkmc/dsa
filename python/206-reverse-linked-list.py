# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if not self.next:
            return str(self.val)
        return f"{self.val}=>{self.next}"


five = ListNode(5, next=None)
four = ListNode(4, next=five)
three = ListNode(3, next=four)
two = ListNode(2, next=three)
one = ListNode(1, next=two)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
        
        
print(Solution().reverseList(one))
