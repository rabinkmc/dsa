class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def f(s):
            stack = []
            for ch in s:
                if ch == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(ch)
            return "".join(stack)
        return f(s) == f(t)

ans = Solution().backspaceCompare("ab#c", "ad#c")
print(ans)
