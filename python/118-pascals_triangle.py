from typing import List
"""
1 
1 1
1 2 1
1 3 3 1
1 4 6 4 1
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = []
        for i in range(1, numRows + 1):
            temp = []
            for j in range(i):
                if j == 0 or j == i - 1:
                    temp.append(1)
                else:
                    temp.append(output[-1][j] + output[-1][j-1])
            output.append(temp)
        return output

print(Solution().generate(5))
