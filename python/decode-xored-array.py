from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        out = [first]
        for ei in encoded:
            out.append(out[-1] ^ ei)
        return out


encoded = [1, 2, 3]
first = 1
ans = Solution().decode(encoded, first)
print(ans)
