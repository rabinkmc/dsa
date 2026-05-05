class Solution:
    def minFlips(self, s: str) -> int:
        """
        for type 1 , we check all rotations
        """
        new = s + s
        n = len(s)
        alt1 = "".join("0" if i % 2 == 0 else "1" for i in range(2 * n))
        alt2 = "".join("1" if i % 2 == 0 else "0" for i in range(2 * n))

        diff1 = 0
        diff2 = 0

        for i in range(n):
            if s[i] != alt1[i]:
                diff1 += 1
            if s[i] != alt2[i]:
                diff2 += 1

        ans = min(diff1, diff2)

        for i in range(n, 2 * n - 1):
            if new[i - n] != alt1[i - n]:
                diff1 -= 1
            if new[i - n] != alt2[i - n]:
                diff2 -= 1
            if new[i] != alt1[i]:
                diff1 += 1
            if new[i] != alt2[i]:
                diff2 += 1
            ans = min(ans, diff1, diff2)
        return ans


s = "111000"
s = "010"
s = "1110"
s = "01001001101"
ans = Solution().minFlips(s)
print(ans)
