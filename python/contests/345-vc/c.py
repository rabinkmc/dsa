from typing import List
class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        nums = [0]*n
        i, color = queries[0]
        nums[i] = color
        out = []
        total = 0
        out.append(total)

        def lc(prev, current, i):
            if i == 0:
                return 0
            left = nums[i-1]
            if prev == left and prev != 0:
                return -1
            if current == left:
                return 1
            return 0

        def rc(prev, current, i):
            if i == n - 1:
                return 0
            right = nums[i+1]
            if prev == right and prev != 0:
                return -1
            if current == right:
                return 1
            return 0

        for i, current in queries[1:]:
            prev = nums[i]
            nums[i] = current
            if prev == current:
                out.append(total)
                continue
            total += lc(prev, current, i) + rc(prev, current, i)
            out.append(total)
        return out

n = 4
queries = [[0,2],[1,2],[3,1],[1,1],[2,1]]
n = 1
queries = [[0,100000]]
ans = Solution().colorTheArray(n, queries)
print(ans)
