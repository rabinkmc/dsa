from typing import List


class Solution:
    def minGenerations(self, points: List[List[int]], target: List[int]) -> int:
        gen = 0
        t1, t2, t3 = target
        n = len(points)
        if n == 1 and points[0] == target:
            return 0
        out = []
        pairs = set()
        ps = [(x, y, z) for (x, y, z) in points]
        while n >= 2:
            out = {(x, y, z) for x, y, z in points}
            for i in range(n):
                x1, y1, z1 = ps[i]
                if t1 == x1 and t2 == y1 and t3 == z1:
                    return gen
                for j in range(i + 1, n):
                    x2, y2, z2 = ps[j]
                    p1, p2, p3 = (x1 + x2) // 2, (y1 + y2) // 2, (z1 + z2) // 2
                    new_pair = (x1, y1, z1, x2, y2, z2)
                    if new_pair in pairs:
                        continue
                    if t1 == p1 and t2 == p2 and t3 == p3:
                        return gen + 1
                    if p1 < t1 or p2 < t2 or p3 < t3:
                        continue
                    pairs.add(new_pair)
                    out.add((p1, p2, p3))
            ps = list(out)
            n = len(ps)
            gen += 1
        return -1


points = [[0, 0, 0], [5, 5, 5]]
target = [1, 1, 1]
points = [[2, 0, 5], [0, 5, 5]]
target = [0, 2, 4]
ans = Solution().minGenerations(points, target)
print(ans)
