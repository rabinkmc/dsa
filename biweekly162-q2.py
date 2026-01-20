from typing import List


def f(x):
    return x[0] + x[1]


def find_t2(t1, arr):
    t2 = 1000000
    for i in range(len(arr)):
        current_time = max(arr[i][0], t1) + arr[i][1]
        t2 = min(t2, current_time)
    return t2


class Solution:
    def earliestFinishTime(
        self,
        ls: List[int],
        ld: List[int],
        ws: List[int],
        wd: List[int],
    ) -> int:
        land = list(zip(ls, ld))
        water = list(zip(ws, wd))
        l, w = min(land, key=f), min(water, key=f)
        case1 = find_t2(f(l), water)
        case2 = find_t2(f(w), land)
        return min(case1, case2)


ls = [2, 8]
ld = [4, 1]
ws = [6]
wd = [3]
ls = [5]
ld = [3]
ws = [1]
wd = [10]
ans = Solution().earliestFinishTime(ls, ld, ws, wd)
print(ans)
