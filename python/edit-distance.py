from functools import lru_cache


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        @lru_cache(None)
        def dfs(i, j):
            ## delete
            if i == m:
                return n - j
            if j == n:
                return m - i
            if word1[i] == word2[j]:
                case1 = dfs(i + 1, j + 1)
                return case1
            remove = 1 + dfs(i + 1, j)
            replace = 1 + dfs(i + 1, j + 1)
            insert = 1 + dfs(i, j + 1)
            return min(remove, replace, insert)

        return dfs(0, 0)


word1, word2 = "horse", "ros"
# word1, word2 = "intention", "execution"
ans = Solution().minDistance(word1, word2)
print(ans)
