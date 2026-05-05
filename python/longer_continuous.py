class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        n = len(s)
        csum = int(s[0] == "1")
        max_one = csum
        for i in range(1, n):
            if s[i] == "1":
                csum += 1
            else:
                max_one = max(max_one, csum)
                csum = 0
        max_one = max(max_one, csum)

        csum = int(s[0] == "0")
        max_zero = csum
        for i in range(1, n):
            if s[i] == "0":
                csum += 1
            else:
                max_zero = max(max_zero, csum)
                csum = 0
        max_zero = max(max_zero, csum)
        return max_one > max_zero


s = "111000011111"
ans = Solution().checkZeroOnes(s)
print(ans)
