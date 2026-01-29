from itertools import permutations

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        p = list(range(1, n+2))
        def check(perm):
            for i in range(n):
                if pattern[i] == 'I' and perm[i+1] <= perm[i]:
                    return False
                if pattern[i] == 'D' and perm[i+1] >= perm[i]:
                    return False
            return True
        for perm in permutations(p):
            if check(perm):
                return "".join(str(x) for x in perm)
        return ""

pattern = "DDD"
ans = Solution().smallestNumber(pattern)
print(ans)
        
