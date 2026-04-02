from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        idx_map = dict()
        for i, item in enumerate(arr):
            idx_map[item] = i
        sz = 0
        print(idx_map)
        for piece in pieces:
            if piece[0] not in idx_map:
                return False
            sz += 1
            for i in range(1, len(piece)):
                x = piece[i]
                if x not in idx_map:
                    return False
                if idx_map[piece[i]] - idx_map[piece[i - 1]] != 1:
                    return False
                sz += 1
        return len(arr) == sz


arr = [15, 88]
pieces = [[88], [15]]
arr = [49, 18, 16]
pieces = [[16, 18, 49]]
arr = [3, 4, 8]
pieces = [[3], [5, 8]]
arr = [37, 69, 3, 74, 46]
pieces = [[37, 69, 3, 74, 46]]
ans = Solution().canFormArray(arr, pieces)
print(ans)
