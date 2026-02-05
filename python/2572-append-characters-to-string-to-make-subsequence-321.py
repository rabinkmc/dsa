# https://leetcode.com/contest/weekly-contest-321/problems/append-characters-to-string-to-make-subsequence/

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        i = 0
        j = 0
        while i < m and j < n:
            if s[i] == t[j]:
                j = j + 1
            i = i + 1
        return n - j
        


print(Solution().appendCharacters(s = "coaching", t = "coding"))
        
