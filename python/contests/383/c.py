# https://leetcode.com/contest/weekly-contest-383/problems/find-the-grid-of-region-average/
from typing import List

# sometimes there is nothing clever, there is just brute force
# I think brute force is very important


class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])

        output = []
        for i in range(m):
            output.append([list() for _ in range(n)])

        def process_grid(i, j):
            if i + 3 > m or j + 3 > n:
                return
            total = 0
            for r in range(i, i + 3):
                for c in range(j, j + 3):
                    total += image[r][c]
                    if r + 1 < i + 3:
                        if abs(image[r][c] - image[r + 1][c]) > threshold:
                            return
                    if c + 1 < j + 3:
                        if abs(image[r][c] - image[r][c + 1]) > threshold:
                            return

            avg = total // 9
            for r in range(i, i + 3):
                for c in range(j, j + 3):
                    output[r][c].append(avg)

        for i in range(m - 2):
            for j in range(n - 2):
                process_grid(i, j)

        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                regions = output[i][j]
                ans[i][j] = sum(regions) // len(regions) if regions else image[i][j]
        return ans


image = [[5, 6, 7, 10], [8, 9, 10, 10], [11, 12, 13, 10]]
threshold = 3
image = [[10, 20, 30], [15, 25, 35], [20, 30, 40], [25, 35, 45]]
threshold = 12
image = [[1, 1, 4, 1], [10, 8, 13, 17], [2, 12, 1, 16]]
threshold = 14
ans = Solution().resultGrid(image, threshold)
print(ans)
