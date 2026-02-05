class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        diffs = [abs(ord(ch1) - ord(ch2)) for ch1, ch2 in zip(s, t)]
        n = len(s)
        total = 0
        i = 0 
        ans = 0
        print(diffs)
        for j in range(n):
            total += diffs[j]
            while total > maxCost:
                total -= diffs[i]
                i = i + 1
            ans = max(ans, j - i + 1)
        return ans
        

s = "abcd"
t = "bcdf"
maxCost = 3
s = "abcd"
t = "cdef"
maxCost = 3
print(Solution().equalSubstring(s, t, maxCost))
