class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        s = [(i, c) for i, c in enumerate(start) if c != 'X']
        e = [(i, c) for i, c in enumerate(result) if c != 'X']
        if len(s) != len(e):
            return False
        print(s, e)
        for (i, c1), (j, c2) in zip(s, e):
            if c1 != c2:
                return False
            if c1 == 'L' and i < j:
                return False
            if c1 == 'R' and i > j:
                return False
        return True

start = "RXXLRXRXL"
result = "XRLXXRRLX"
ans = Solution().canTransform(start, result)
print(ans)
