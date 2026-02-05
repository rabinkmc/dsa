class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        n1 = len(a)
        n2 = len(b)
        if b in a:
            return 1
        # b not in a and n1 > n2
        if n2 < n1:
            return -1

        if a == b:
            return 1

        if a not in b:
            return -1

        k = n2 // n1
        if n2 % n1 == 0:
            substr = a * k 
        else:
            k = k + 1
            substr = a * k

        if b in substr:
            return k

        if b in (substr + a):
            return k + 1
        return -1

a = "abc"
b = "cabcabca"
ans = Solution().repeatedStringMatch(a, b)
print(ans)
