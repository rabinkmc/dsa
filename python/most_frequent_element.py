from typing import List


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        counter = dict()
        ans = -1
        for num in nums:
            if num % 2 == 1:
                continue
            counter[num] = counter.get(num, 0) + 1
            if ans == -1:
                ans = num
            else:
                if counter[num] == counter[ans]:
                    if num < ans:
                        ans = num
                elif counter[num] > counter[ans]:
                    ans = num
        return ans


nums = [0, 1, 2, 2, 4, 4, 1]
nums = [4, 4, 4, 9, 2, 4]
nums = [29, 47, 21, 41, 13, 37, 25, 7]
ans = Solution().mostFrequentEven(nums)
print(ans)
