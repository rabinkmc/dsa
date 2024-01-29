# https://leetcode.com/contest/weekly-contest-325/problems/maximum-tastiness-of-candy-basket/
# price = [13,5,1,8,21,2], k = 3
# Output: 8
from typing import List


def check(guess, k, arr):
    """
    I need to prove that there are at least k numbers which have a minimum difference of the guessed answer

    how do I find k numbers, to find k numbers I need to do k - 1 comparisons and verify k - 1 comparisons return true
    if a1 - a2 >= d and a2 - a3 >= d it also means a1 - a3 >= d
    """
    count = 1
    last = arr[0]
    for i in range(1, len(arr)):
        # idea is to check consecutive pairs that satisfy the condition

        if arr[i] - last >= guess:
            last = arr[i]
            count += 1
            if count == k:
                return True
    return False


class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        left = 0
        right = price[-1] - price[0]
        ans = 0
        while left <= right:
            mid = left + (right - left) // 2
            if check(mid, k, price):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans


price = [1, 3, 1]
k = 2
price = [13, 5, 1, 8, 21, 2]
k = 3
ans = Solution().maximumTastiness(price, k)
print(ans)
