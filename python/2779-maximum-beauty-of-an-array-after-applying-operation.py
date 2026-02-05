from typing import List


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        left = 0
        ans = -1
        right = 0
        while right < n:
            while right < n and nums[right] - nums[left] <= 2 * k:
                ans = max(ans, right - left + 1)
                right += 1
            left += 1

        return ans


nums = [4, 6, 1, 2]
k = 2
nums = [1, 1, 1, 1]
k = 0
# idea, is to sort the array
# keep making the window bigger as long as the condition holds
# what is the condition, to make all the same elements in the same window by increasing or decreasing any particular number in the range from -k to k
# so that means, we can make the smallest number, l + k, biggest , r - k and if r - l <= 2*k that means we can increase the l and decrease the r
ans = Solution().maximumBeauty(nums, k)
print(ans)
