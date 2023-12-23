from typing import List
from collections import Counter


class Solution:
    def minGroupsForValidAssignment(self, nums: List[int]) -> int:
        counter = Counter(nums)
        min_size = counter.most_common()[-1][1]
        max_size = min_size + 1
        ans = 0
        print(counter)
        for key, count in counter.items():
            print(key, count)
            if (count / max_size) >= 1:
                group = (count / max_size).__ceil__()
            else:
                group = (count / min_size).__ceil__()
            ans += group
        return ans


nums = [10, 10, 10, 3, 1, 1]
nums = [3,2,3,2,3]
nums = [1,1,3,3,1,1,2,2,3,1,3,2]
ans = Solution().minGroupsForValidAssignment(nums)
