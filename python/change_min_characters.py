from collections import Counter


class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        m, n = len(a), len(b)
        ca = [0] * 26
        cb = [0] * 26
        for key in a:
            ca[ord(key) - ord("a")] += 1
        for key in b:
            cb[ord(key) - ord("a")] += 1
        res = m + n - max(ca[i] + ca[i] for i in range(26))
        for i in range(25):
            # this is saying let's make all the characters greater than say 'd'
            # i == 4
            # so, we know ca[i] means all the characters that are less than or equal to d
            # to make a < b, we know ca[i] is already less than i so, we have to change the r# remaining characters and for cb[i], these are the characters than are less than or equal to 'd' we have to change that
            # suppose 'z', we are trying to make cb greater than 'z', not possible
            case1 = (m - ca[i]) + cb[i]  # a < b
            case2 = (n - cb[i]) + ca[i]  # b < a
            ca[i + 1] += ca[i]  # carrying along the prefix sum
            cb[i + 1] += cb[i]  # carrying along the prefix sum

            res = min(res, case1, case2)
        return res


a, b = "aba", "caa"
# a = "dabadd"
# b = "cda"
a = "da"
b = "cced"
ans = Solution().minCharacters(a, b)
print(ans)
