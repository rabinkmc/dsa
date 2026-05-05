from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a, b, c = target
        out = []
        for x, y, z in triplets:
            if x > a or y > b or z > c:
                continue
            out.append([x, y, z])
        if not out:
            return False
        curr = out[0]
        for i in range(1, len(out)):
            maxa = max(curr[0], out[i][0])
            maxb = max(curr[1], out[i][1])
            maxc = max(curr[2], out[i][2])
            curr = [maxa, maxb, maxc]
        return curr == target


triplets = [[2, 5, 3], [1, 8, 4], [1, 7, 5]]
target = [2, 7, 5]
triplets = [[1, 3, 1]]
target = [1, 3, 1]
ans = Solution().mergeTriplets(triplets, target)
print(ans)
