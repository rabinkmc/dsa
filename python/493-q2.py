class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0

        digits = 0
        num = n
        while num:
            digits += 1
            num = num // 10

        ans = 0
        for i in range(3, digits-1):
            max_num = 10**(i+1) - 1
            min_num = 10**(i)
            ans += (max_num - min_num + 1) * (i // 3)
        tmp = (n- 10**(digits - 1) + 1) * ((digits-1) // 3)
        ans += tmp
        return ans





ans = Solution().countCommas(154729)
print(ans)
        
