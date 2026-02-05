class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val}->{self.next}"


def build_list(arr):
    prev = None
    n = len(arr)
    for i in range(n - 1, -1, -1):
        prev = ListNode(val=arr[i], next=prev)
    return prev
