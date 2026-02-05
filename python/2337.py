class Solution:
    def canChange(self, start: str, target: str) -> bool:
        s = [(i, c) for i, c in enumerate(start) if c != '_']
        e = [(i, c) for i, c in enumerate(target) if c != '_']
        if len(s) != len(e):
            return False
        for (i, c1), (j, c2) in zip(s,e):
            if c1 != c2:
                return False
            if c1 == "L" and i < j:
                return False
            if c1 == "R" and i > j:
                return False
        return True

start = "_L__R__R_"
target = "L______RR"
ans = Solution().canChange(start, target)
print(ans)
        
