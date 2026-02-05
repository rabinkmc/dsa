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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        dummy = prev = ListNode(-101, next=curr)
        while curr:
            if curr.val == prev.val:
                curr = curr.next
                continue

            temp = ListNode(curr.val)
            prev.next = temp
            prev = temp
            curr = curr.next
        return dummy.next


three2 = ListNode(3)
three1 = ListNode(3, next=three2)
two = ListNode(2, next=three1)
one2 = ListNode(1, next=two)
one1 = ListNode(1, next=one2)

pprint(Solution().deleteDuplicates(one1))
