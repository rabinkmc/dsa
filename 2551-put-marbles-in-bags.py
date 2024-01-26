from typing import List

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        pair_weights = []
        n = len(weights)
        for i in range(n-1):
            pair_weights.append(weights[i] + weights[i+1])
        pair_weights.sort()
        # k - 1 small pairwise weights 
        # we need to take k - 1 elements
        if k == 1:
            return 0
        k_1_minw = sum(pair_weights[:k-1])
        # k - 1 large pairwise weights
        k_1_maxw = sum(pair_weights[-k+1:])
        return k_1_maxw - k_1_minw

weights = [25,74,16,51,12,48,15,5]
k = 1
ans = Solution().putMarbles(weights, k)
print(ans)
