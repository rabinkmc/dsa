from typing import Optional


class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __str__(self):
        if not self.next:
            return f"{self.val}"
        return f"{self.val}->{self.next}"

    def __repr__(self):
        return str(self)


one = Node(1, next=None)
ten = Node(10, next=one)
eleven = Node(11, next=ten)
thirteen = Node(13, next=eleven)
seven = Node(7, next=thirteen)


def pprint(node):
    while node:
        print(node.val, "->", node.random and node.random.val)
        node = node.next


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        curr = head
        out = newHead = Node(-1)
        map = {}

        while curr:
            temp = Node(curr.val)
            out.next = temp
            map[curr] = temp

            out = temp
            curr = curr.next

        for node, clone in map.items():
            if node.random:
                clone.random = map[node.random]

        return newHead.next


ans = Solution().copyRandomList(seven)
pprint(ans)
