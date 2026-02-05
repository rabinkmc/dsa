def is_adj(a, b):
    dist = abs(ord(a) - ord(b))
    return dist == 1 or dist == 25


class Solution:
    def resultingString(self, s: str) -> str:
        stack = []
        for ch in s:
            if stack and is_adj(stack[-1], ch):
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)


s = "abc"
s = "zadb"
ans = Solution().resultingString(s)
print(ans)
