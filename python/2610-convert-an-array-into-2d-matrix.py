from typing import List

nums = [1,3,4,1,2,3,1]
nums = [1, 1, 1, 1, 1, 1, 1]

# maintain a counter to keep track of the count of the element
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        counter = dict()
        output = [[]]
        for num in nums:
            counter[num] = counter.get(num, -1) + 1
            idx = counter[num]
            if idx < len(output):
                output[idx].append(num)
            else:
                output.append([num])

        return output

ans = Solution().findMatrix(nums)
print(ans)

        
