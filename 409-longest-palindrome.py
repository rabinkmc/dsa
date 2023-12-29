from collections import defaultdict

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = defaultdict(int)
        total = 0
        for ch in s:
            counter[ch] += 1
            if counter[ch] == 2:
                total += 2  
                counter[ch] = 0
        return total + int(1 in counter.values())

assert Solution().longestPalindrome(s = "abccccdd") == 7, Solution().longestPalindrome(s = "abccccdd")
