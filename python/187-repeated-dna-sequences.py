from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        L = 10
        if n < L:
            return []

        int_map = {"A": 0, "C": 1, "G": 2, "T": 3}
        nums = [int_map[x] for x in s]

        h = 0
        for i in range(L):
            h = h * 4 + nums[i]

        output = set()
        seen = set()
        seen.add(h)
        base = 4
        for start in range(1, n - L + 1):
            h = h * base - nums[start - 1] * pow(base, L) + nums[start + L - 1]
            if h in seen:
                output.add(s[start : start + L])
            seen.add(h)
        return list(output)


s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print(Solution().findRepeatedDnaSequences(s))
