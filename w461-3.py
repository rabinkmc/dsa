from typing import List


class Solution:
    def minTime(self, s: str, order: List[int], k: int) -> int:
        n = len(order)
        left, right = 0, n - 1
        subcount = lambda x: (x * (x + 1)) // 2
        total_subarrays = subcount(n)

        def valid_count(mid):
            l = list(s)
            for t in range(mid + 1):
                i = order[t]
                l[i] = "*"
            non_star = 0
            count = 0
            for ch in l:
                if ch != "*":
                    non_star += 1
                else:
                    count += subcount(non_star)
                    non_star = 0
            count += subcount(non_star)
            return total_subarrays - count

        ans = -1
        while left <= right:
            mid = left + (right - left) // 2
            curr = valid_count(mid)
            if curr >= k:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans


s = "cat"
order = [0, 2, 1]
k = 6
ans = Solution().minTime(s, order, k)
print(ans)
