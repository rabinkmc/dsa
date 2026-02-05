from typing import List

class Solution:
    def partitionString(self, s: str) -> List[str]:
        seen = set()
        i = 0
        current = []
        ans = []
        def f(x):
            return "".join(x)
        for j in range(len(s)):
            current.append(s[j])
            l = f(current)
            if l not in seen:
                seen.add(l)
                ans.append(l)
                current = []
        return ans

s = "abbccccd"
ans = Solution().partitionString(s)
print(ans)
        
