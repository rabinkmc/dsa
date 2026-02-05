class Solution:
    def punishmentNumber(self, n: int) -> int:
        def check(num, target, i, total):
            if i == len(num):
                if total == target:
                    return True

            for next_i in range(i + 1, len(num) + 1):
                if i == 0 and next_i == len(num):
                    continue
                if check(num, target, next_i, total + int(num[i:next_i])):
                    return True
            return False

        ans = 1
        for i in range(2, n+1):
            if check(str(i*i), i,0, 0):
                ans += i * i 
        return ans


n = 1000
ans = Solution().punishmentNumber(n)
print(ans)
