class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = c // 2
        ans = False

        def check(num):
            left = 0
            right = num // 2
            while left <= right:
                m = left + (right - left) // 2
                if m * m == num:
                    return True
                if m * m > num:
                    right = m - 1
                else:
                    left = m + 1
            return False

        while left <= right:
            m = left + (right - left) // 2
            a2 = m * m
            if a2 > m:
                right = m - 1
                continue

            b2 = c - a2
            if check(b2):
                return True
            elif a2 < m:

        return False


ans = Solution().judgeSquareSum(5)
print(ans)
