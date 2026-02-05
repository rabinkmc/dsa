from collections import Counter


class Solution:
    def largestPalindromic(self, num: str) -> str:
        counter = Counter(num)
        l = []
        for x in "987654321":
            l.append((counter[x] // 2) * x)
        res = "".join(l).lstrip("0")
        mid = "0"
        for x in counter:
            if counter[x] % 2 == 1:
                mid = max(mid, x)

        return res + mid + res[::-1]


ans = Solution().largestPalindromic(num)
print(ans)
