from typing import List


class Solution2:
    variables = [[2, 3, 3, 10], [3, 3, 3, 1], [6, 1, 1, 4]]
    target = 2

    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        def f(a, b, c, d):
            return (((a**b) % 10) ** c) % d

        answer = []
        for i, (a, b, c, d) in enumerate(variables):
            print(f(a, b, c, d))
            if f(a, b, c, d) == target:
                answer.append(i)
        return answer


class Solution3:
    def slidingWindow(self, nums, k):
        _max = max(nums)
        count = 0
        total = 0
        i = 0
        for j in range(len(nums)):
            count += nums[j] == _max
            print((i, j), nums[i : j + 1])
            while count >= k:
                count -= nums[i] == _max
                i = i + 1
            total += i

        print("count", count)
        return total


nums = [1, 3, 2, 3, 3]
k = 2

Solution3().slidingWindow(nums, k)
