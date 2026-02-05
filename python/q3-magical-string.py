class Solution:
    def magicalString(self, n: int) -> int:
        if n <= 3:
            return 1
        # n = 3, 122
        # n = 2, 12
        # n = 1, 1
        s = "122"
        next = 1
        i = 3
        while len(s) <= n:
            s = s + str(next) * int(s[i-1])
            i = i + 1
            next = 3 - next

        return s[:n].count("1")

n = 8
ans = Solution().magicalString(n)
print(ans)
        
