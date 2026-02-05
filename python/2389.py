from typing import List

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        psum = [0]*(n + 1)
        for i in range(n):
            psum[i+1] = psum[i] + nums[i]

        def bsearch(target):
            left = 0
            right = n 
            ans = -1
            while left <= right:
                mid = left + (right - left) // 2
                if psum[mid] <= target:
                    ans = mid
                    left = mid + 1
                else:
                    right = mid - 1
            return ans

        ans = []
        for query in queries:
            idx = bsearch(query)
            ans.append(idx)
        return ans

nums = [4,5,2,1]
queries = [3, 10, 21]
ans = Solution().answerQueries(nums, queries)
print(ans)
        
