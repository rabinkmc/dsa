from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, next=head)
        nodes = [dummy]
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        idx = len(nodes) - n

        nodes[idx - 1].next = nodes[idx].next
        return dummy.next


def pprint(node):
    while node:
        print(node.val, end="->")
        node = node.next
    print()


root = ListNode(
    val=1, next=ListNode(val=2, next=ListNode(3, next=ListNode(4, next=ListNode(5))))
)

pprint(root)

pprint(Solution().removeNthFromEnd(root, 5))
