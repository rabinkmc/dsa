from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val}=>{self.next}"


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # find the middle pointer
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # now it is time to reverse the back part of the linked list
        # slow + 1 until end

        # reverse the linked list starting from the middle as head
        prev = None
        cur = slow
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        # now prev is the reversed head
        # now iterate from head, and reversed middle head
        back = prev
        front = head
        while back:
            print(front.val, back.val)
            if front.val != back.val:
                return False
            back = back.next
            front = front.next
        return True

f6 = ListNode(1)
f5 = ListNode(2, next=f6)
f4 = ListNode(3, next=f5)
f3 = ListNode(3, next=f4)
f2 = ListNode(2, next=f3)
f1 = ListNode(1, next=f2)
solution = Solution().isPalindrome(f1)
assert solution == True, solution
