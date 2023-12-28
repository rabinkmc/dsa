def fn(head):
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


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val}->{self.next}"


three = Node(3)
two = Node(2, next=three)
one = Node(1, next=two)

rev = fn(one)
print(rev)
