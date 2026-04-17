# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


five = ListNode(5)
four = ListNode(4, next=five)
three = ListNode(3, next=four)
two = ListNode(2, next=three)
one = ListNode(1, next=two)


def pprint(node):
    while node:
        print(node.val, end="->")
        node = node.next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = []
        curr = head
        n = 0
        while curr:
            temp.append(curr.val)
            curr = curr.next
        ## begin: k - 1
        ## end: n - k
        n = len(temp)
        temp[k - 1], temp[n - k] = temp[n - k], temp[k - 1]
        dummy = ListNode(-1)
        curr = dummy
        for val in temp:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next


ans = Solution().swapNodes(one, 2)
pprint(ans)
