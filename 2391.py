from typing import List


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        glasses = []
        metals = []
        papers = []

        n = len(garbage)
        travel_cost = [0] * n
        for i in range(n - 1):
            travel_cost[i + 1] = travel_cost[i] + travel[i]

        for i, g in enumerate(garbage):
            glass = g.count("G")
            paper = g.count("P")
            metal = g.count("M")
            if glass:
                glasses.append((i, glass))
            if paper:
                papers.append((i, paper))
            if metal:
                metals.append((i, metal))

        def gcost(garbage):
            if not garbage:
                return 0
            final_idx = -1
            pickup_cost = 0
            for idx, count in garbage:
                pickup_cost += count
                final_idx = idx
            return pickup_cost + travel_cost[final_idx]

        return gcost(glasses) + gcost(metals) + gcost(papers)


garbage = ["G", "P", "GP", "GG"]
travel = [2, 4, 3]
ans = Solution().garbageCollection(garbage, travel)
print(ans)
