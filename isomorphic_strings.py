class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map1 = dict()
        map2 = dict()
        for c1, c2 in zip(s, t):
            if (c1 not in map1) and (c2 not in map2):
                map1[c1] = c2
                map2[c2] = c1
                continue
            if c1 in map1 and map1[c1] != c2:
                return False
            if c2 in map2 and map2[c2] != c1:
                return False
        return True

s, t = "badc", "baba"
ans = Solution().isIsomorphic(s, t)
print(ans)
        
