from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: (-x[1], -x[0]))
        ans = 0
        rem = truckSize
        i = 0
        while i < len(boxTypes) and rem > 0:
            curr_boxes, value = boxTypes[i]
            if curr_boxes > rem:
                ans = ans + rem * value
                return ans
            rem = rem - curr_boxes
            ans = ans + curr_boxes * value
            i += 1
        return ans


boxTypes = [[1, 3], [2, 2], [3, 1]]
truckSize = 4
ans = Solution().maximumUnits(boxTypes, truckSize)
print(ans)
