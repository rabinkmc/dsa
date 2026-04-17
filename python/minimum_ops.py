from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        indices = []
        for i in range(n):
            if boxes[i] == "1":
                indices.append(i)
        print(indices)
        out = []
        for i in range(n):
            tmp = 0
            for j in indices:
                tmp += abs(i - j)
            out.append(tmp)
        return out


boxes = "001011"
ans = Solution().minOperations(boxes)
print(ans)
