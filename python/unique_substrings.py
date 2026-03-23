class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        self.seen = set()
        self.ans = 0

        def backtrack(i):
            if i == n:
                self.ans = max(self.ans, len(self.seen))
                return
            for j in range(i + 1, n + 1):
                substr = s[i:j]
                if substr not in self.seen:
                    self.seen.add(substr)
                    backtrack(j)
                    self.seen.remove(substr)

        backtrack(0)

        return self.ans


s = "wwwzfvedwfvhsww"
# s = "wwwzfvedwfvhsww"
ans = Solution().maxUniqueSplit(s)
print(ans)
