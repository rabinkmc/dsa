from typing import List

def merge(nums, left, m, right):
    n1 = (m - left + 1)
    n2 = (right - m)

    left_arr = nums[left:m+1]
    right_arr = nums[m+1:right+1]

    i = 0 
    j = 0 
    for k in range(left, right+1):
        if (j >= n2) or ((i < n1) and left_arr[i] <= right_arr[j]):
            nums[k] = left_arr[i]
            i = i+ 1
        else:
            nums[k] = right_arr[j]
            j = j + 1

def f(nums,left,right):
    if left >= right:
        return 0
    m = left + (right - left) // 2
    count = f(nums, left, m) + f(nums, m+1, right)

    j = m + 1
    for i in range(left, m+1):
        while (j <= right) and nums[i] > (nums[j] * 2):
            j = j + 1
        count += j - (m+1)
    merge(nums, left, m, right)
    return count


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return f(nums, 0, len(nums)-1)

nums = [1, 3, 2, 3, 1]
ans = Solution().reversePairs(nums)
print(ans)
        
