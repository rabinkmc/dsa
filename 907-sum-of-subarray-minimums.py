"""
wiki:
S = new empty stack data structure
for x in the input sequence do
    while S is nonempty and the top element of S is greater than or equal to x do
        pop S
    if S is empty then
        x has no preceding smaller value
    else
        the nearest smaller value to x is the top element of S
    push x onto S
"""
from typing import List
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 1000_000_000 + 7
        n = len(arr)
        stack = []
        left = [-1]*n
        right = [n]*n
        for i, x in enumerate(arr):
            while stack and arr[stack[-1]] >= x:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        stack = []
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)

        total = 0
        for i in range(n):
            total += (i - left[i]) * (right[i] - i) * arr[i]
        return total % mod

arr1 = [71,55,82,55]
ans = Solution().sumSubarrayMins(arr = arr1)
print(ans)
