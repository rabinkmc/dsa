from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p = "".join(sorted(list(p)))
        print()
        k = len(p)
        n = len(s)
        ans = []
        for i in range(n - k + 1):
            substr = s[i : i + k]
            curr = "".join(sorted(substr))
            if curr == p:
                ans.append(i)
        return ans


s = "cbaebabacd"
p = "abc"
ans = Solution().findAnagrams(s, p)
print(ans)
