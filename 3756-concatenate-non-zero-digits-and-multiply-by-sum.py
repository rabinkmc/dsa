from typing import List

def f(s):
    for ch in s:
        ans = 

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        csum = 0
        psum = []
        for ch in s:
            csum += int(ch)
            psum.append(csum)

        return []


s = "10203004"
queries = [[0, 7], [1, 3], [4, 6]]
ans = Solution().sumAndMultiply(s, queries)
print(ans)
