from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        curr = [1]
        for row in range(1, rowIndex+1):
            tmp = [0] * (row + 1)
            tmp[0] = 1
            tmp[-1] = 1
            for col in range(1, row):
                tmp[col] = curr[col-1] + curr[col]
            curr = tmp[:]
        return curr

ans = Solution().getRow(0)
print(ans)
