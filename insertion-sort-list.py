# Definition for singly-linked list.
from typing import Optional


def pprint(node):
    while node:
        print(node.val, end="->")
        node = node.next


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next

        def insertion_sort(arr):
            n = len(arr)
            for i in range(1, n):
                j = i - 1
                temp = arr[i]
                while j >= 0 and temp < arr[j]:
                    arr[j + 1] = arr[j]
                    j = j - 1
                arr[j + 1] = temp
            return arr

        arr = insertion_sort(arr)

        curr = dummy = ListNode(0)
        for num in arr:
            curr.next = ListNode(num)
            curr = curr.next
        return dummy.next


four = ListNode(4)
two = ListNode(2, four)
seven = ListNode(7, two)
eight = ListNode(8, seven)
one = ListNode(1, eight)
three = ListNode(3, one)
five = ListNode(5, three)
six = ListNode(6, five)
pprint(Solution().insertionSortList(six))
