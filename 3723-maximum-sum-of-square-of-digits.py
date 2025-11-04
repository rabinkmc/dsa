class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if 9 * num < sum:
            return ""
        rem = sum % 9
        nines = sum // 9
        ans = "9" * nines + (str(rem) if rem else "")
        if len(ans) < num:
            ans = ans + "0" * (num - len(ans))
        return ans


print(Solution().maxSumOfSquares(5, 28))
