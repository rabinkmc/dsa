class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for x in num:
            while k and stack and stack[-1] > x:
                stack.pop()
                k -= 1
            stack.append(x)

        if k:
            stack = stack[:-k]  # remove last k elements

        # removing trailing zeros
        ans = "".join(stack).lstrip("0")
        return ans if ans else "0"


num = "1432219"
k = 3
# idea is to have create a monotonic increasing stack from left to right removing k elements
# during the process if k elements are removed , we stop processing further
# 1432219
# -> 1
# -> 1->4
# -> 1->3 (pop 4)
# -> 1->2 (pop 2, k = 2)
# -> 1->2->2
# -> 1->2->1(pop 1, k = 3)

ans = Solution().removeKdigits(num, k)
print(ans)
