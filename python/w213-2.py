class Solution:
    def countVowelStrings(self, n: int) -> int:
        self.ans = 0

        graph = {"a": "aeiou", "e": "eiou", "i": "iou", "o": "ou", "u": "u"}

        def backtrack(node, curr):
            if len(curr) == n:
                self.ans += 1
                return
            for adj in graph[node]:
                backtrack(adj, curr + adj)

        backtrack("a", "")
        return self.ans


n = 1
ans = Solution().countVowelStrings(n)
print(ans)
