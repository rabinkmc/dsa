from typing import List
from collections import deque


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        ec = 0
        for i in range(n):
            nums[i] = int(nums[i] % 2 == 0)
            ec += nums[i]
        if abs(ec - (n - ec)) >= 2:
            return -1

        ei = deque()
        oi = deque()
        for i in range(n):
            if nums[i] == 1:
                ei.append(i)
            else:
                oi.append(i)

        print(oi, ei)

        more_even = ec > n - ec

        def parity_count(ei, oi, more_even=True):
            ans = 0
            if more_even:
                for i in ei:
                    swapi = -1
                    if i % 2 == 0:
                        continue
                    swapi = oi.popleft()
                    nums[i], nums[swapi] = nums[swapi], nums[i]
                    ans += abs(i - swapi)
                return ans

            for i in oi:
                swapi = -1
                if i % 2 == 1:
                    continue
                swapi = ei.popleft()
                nums[i], nums[swapi] = nums[swapi], nums[i]
                ans += abs(i - swapi)
            return ans

        if n % 2 == 1:
            return parity_count(ei, oi, more_even)
        else:
            return min(parity_count(ei, oi, True), parity_count(ei, oi, False))


nums = [2, 4, 6, 5, 7]
print(Solution().minSwaps(nums))
