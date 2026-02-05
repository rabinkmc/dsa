from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.memo = {}
        def helper(s, wordDict):
            if s in self.memo:
                return self.memo[s]
                
            if not s:
                self.memo[s] = True
                return True
            for word in wordDict:
                if not s.startswith(word):
                    continue
                if helper(s[len(word) :], wordDict):
                    self.memo[s] = True
                    return True
            self.memo[s] = False
            return self.memo[s]

        return helper(s, wordDict)


wordDict = ["leet", "code"]
ans = Solution().wordBreak("leetcode", wordDict)
assert ans == True
ans = Solution().wordBreak(s="applepenapple", wordDict=["apple", "pen"])
assert ans == True
ans = Solution().wordBreak(
    s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]
)
assert ans == False
