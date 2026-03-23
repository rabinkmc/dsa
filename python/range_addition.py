from typing import List
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        arr = [0] * (length + 1)

        for start, end, val in updates:
            arr[start] += val
            arr[end + 1] -= val

        for i in range(1, length):
            arr[i] += arr[i-1]
        return arr[:length]

        
