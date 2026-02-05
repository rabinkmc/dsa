class Solution:
    def convertToBase7(self, num: int) -> str:
        res = []
        sign = -1 if num < 0 else 1
        num = abs(num)
        if num == 0:
            return "0"
        while num:
            rem = num % 7
            res.append(str(rem))
            num = num // 7
        out = "".join(res)
        if sign == -1:
            return "-" + out[::-1]
        return out[::-1]
ans = Solution().convertToBase7(0)
print(ans)
        
