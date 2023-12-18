import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1 = len(str1)
        l2 = len(str2)
        answer = ""
        for i in range(1, min(l1, l2) + 1):
            if l1 % i or l2 % i:
                continue
            n1, n2 = l1 // i, l2 // i
            if str1[:i] * n1 == str1 and str1[:i] * n2 == str2:
                answer = str1[:i]
        return answer


str1 = "ABABAB"
str2 = "AB"

print(Solution().gcdOfStrings(str1, str2))
