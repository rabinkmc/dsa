from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * n
        for i in range(n):
            for word in wordDict:
                # check if is the end index of the word
                lw = len(word)
                if i < lw:
                    continue
                substr = s[i - lw + 1 : i + 1]
                if word == substr and (i - lw < 0 or dp[i - lw] == True):
                    dp[i] = True
                    break

        return False
