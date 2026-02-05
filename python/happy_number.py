def happy(n):
    res = 0
    while n:
        rem = n % 10
        res = res + rem * rem
        n = n // 10
    return res

class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        x = n
        while x != 1:
            if x in visited:
                return False
            visited.add(x)
            x = happy(x)
        return True

print(Solution().isHappy(2))
