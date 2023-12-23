class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        sum1 = 0
        sum2 = 0
        for num in range(1, n + 1):
            if num % m == 0:
                sum2 += num
            else:
                sum1 += num
        return sum1 - sum2
