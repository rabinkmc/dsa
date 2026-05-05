class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)

        def f(x):
            if all(xi == "0" for xi in x):
                return 0
            return int(x.lstrip("0"))

        self.ans = False

        def backtrack(curr, i):
            if self.ans:
                return
            if i == n:
                self.ans = len(curr) >= 2
                return
            for j in range(i, n):
                if not curr:
                    tmp = f(s[i : j + 1])
                    backtrack(curr + [tmp], j + 1)
                else:
                    tmp = f(s[i : j + 1])
                    if curr[-1] - tmp == 1:
                        backtrack(curr + [tmp], j + 1)

        backtrack([], 0)

        return self.ans


s = "1234"
# s = "050043"
ans = Solution().splitString(s)
print(ans)
