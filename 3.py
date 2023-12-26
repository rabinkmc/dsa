from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = defaultdict(int)
        left = right = ans = 0
        while right < len(s):
            ch = s[right]
            counter[ch] += 1
            while counter[ch] > 1:
                counter[s[left]] -= 1
                left += 1
            ans = max(right - left + 1, ans)
            right += 1
        return ans


s = "pwwkew"
ans = Solution().lengthOfLongestSubstring(s)
print(ans)
