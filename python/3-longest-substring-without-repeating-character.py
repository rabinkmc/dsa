from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0 
        counter = defaultdict(int)
        ans = 0
        for j, ch in enumerate(s):
            counter[ch] += 1
            while counter[ch] > 1:
                counter[s[i]] -= 1
                i = i + 1
            ans = max(ans, j - i + 1)
        return ans

ans = Solution().lengthOfLongestSubstring(s = "abcabcbb")
print(ans)


        
