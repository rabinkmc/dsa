from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        wsum = sum(arr[:k])
        threshold = threshold * k
        ans = 0
        if wsum >= threshold:
            ans += 1

        n = len(arr)
        for i in range(1, n - k + 1):
            wsum = wsum + arr[i + k - 1] - arr[i - 1]
            if wsum >= threshold:
                ans += 1
        return ans


arr = [11, 13, 17, 23, 29, 31, 7, 5, 2, 3]
k = 3
threshold = 5
print(Solution().numOfSubarrays(arr, k, threshold))
