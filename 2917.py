from typing import List
from collections import defaultdict

# brute force solution


class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        bits = defaultdict(int)
        maximum = max(nums)
        length = 0
        while maximum:
            maximum = maximum // 2
            length += 1

        for i in range(length):
            for num in nums:
                bit = (num >> i) & 1
                if bit:
                    bits[i] += 1

        ans = 0
        print(bits)
        for i in bits:
            if bits[i] >= k:
                ans += 2**i
        return ans


nums = [7, 12, 9, 8, 9, 15]
# nums = [2, 12, 1, 11, 4, 5]
k = 1
nums = [16]
print(Solution().findKOr(nums, k))
