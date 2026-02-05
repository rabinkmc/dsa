def fn(head):
    slow = head
    fast = head
    ans = 0
    while fast and fast.next:
        slow = slow.next
        fast = fast.next
    return ans
