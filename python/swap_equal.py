class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if sorted(s1) != sorted(s2):
            return False
        count = 0
        n = len(s1)
        for i in range(n):
            count += int(s1[i] != s2[i])
        return count <= 2
