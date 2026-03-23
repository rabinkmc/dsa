from typing import List

class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        def swap_player(player):
            return 1 - player
        n = len(nums)
        player = 0
        scores = [0, 0]
        for i in range(n):
            if nums[i] % 2 == 1:
                player = swap_player(player)
            if (i + 1) % 6 == 0:
                player = swap_player(player)
            scores[player] += nums[i]
        return scores[0] - scores[1]

nums = [2,4,2,1,2,1]
nums = [1]
ans = Solution().scoreDifference(nums)
print(ans)
