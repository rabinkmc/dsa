class Solution:
    def countCommas(self, n: int) -> int:
        def f(n):
            ans = 0
            while n >= 1000:
                ans += 1
                n = n // 1000
            return ans
        commas = 0
        for i in range(1000, n+1):
            commas += f(i)
        return commas


ans = Solution().countCommas(1002)
print(ans)
        
