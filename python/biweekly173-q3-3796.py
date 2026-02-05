from typing import List


class Solution:
    def findMaxVal(self, n: int, restrictions: List[List[int]], diff: List[int]) -> int:
        psum = [0] * (len(diff) + 1)
        psum[0] = 0
        psum[1] = diff[0]
        csum = 0
        for i in range(0, len(diff)):
            csum += diff[i]
            psum[i + 1] = csum
        ans = 0
        for idx in range(len(restrictions)):
            i, maxi = 0, 0
            if idx > 0:
                i, maxi = restrictions[idx - 1][0], restrictions[idx - 1][1]
            j, maxj = restrictions[idx]
            diffsum = psum[j] - psum[i]
            if maxi + diffsum < maxj:
                return -1
            csum = maxi
            cmax = -1
            if j == 8:
                print(csum)
            while i <= j and 2 * csum - diffsum <= maxj:
                cmax = max(csum, cmax)
                csum += diff[i]
                i = i + 1
            ans = max(ans, cmax)
        max_idx = max(restrictions)
        i = max_idx[0]
        if i < n:
            i = max_idx[0]
            suffix_sum = psum[n - 2] - psum[i]
            ans = max(ans, max_idx[1] + suffix_sum)
        return ans


n = 10
restrictions = [[3, 1], [8, 1]]
diff = [2, 2, 3, 1, 4, 5, 1, 1, 2]
# n = 8
# restrictions = [[3, 2]]
# diff = [3, 5, 2, 4, 2, 3, 1]
# n  2
# restrictions = [[1, 15]]
# diff = [2]
ans = Solution().findMaxVal(n, restrictions, diff)
print(ans)
