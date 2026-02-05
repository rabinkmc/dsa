class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        i = 0
        prefix = ""
        while i < len(s1) and i < len(s2) and i < len(s3) and (s1[i] == s2[i] == s3[i]):
            prefix += s1[i]
            i = i + 1
        return len(s1) + len(s2) + len(s3) - 3 * len(prefix)

    def minimumSteps(self, s: str) -> int:
        st = list(s)
        ones = [i for i, ch in enumerate(st) if ch == "1"]
        one_start = len(st) - len(ones)
        return sum(range(one_start, len(st))) - sum(ones)

    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        number = 0
        for i in range(n - 1, -1, -1):
            print(i)
            bita = a >> i & (2**n - 1)
            bitb = b >> i & (2**n - 1)
            if bita == bitb == 0:
                number += 2**i

        print(bin(a))
        print(bin(b))
        print(bin(number))


s1 = "abc"
s2 = "abb"
s3 = "ab"
# print(Solution().findMinimumOperations(s1, s2, s3))
s = "101"
# print(Solution().minimumSteps(s))

Solution().maximumXorProduct(1, 6, 3)
