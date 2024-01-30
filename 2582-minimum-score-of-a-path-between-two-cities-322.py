# https://leetcode.com/contest/weekly-contest-322/problems/minimum-score-of-a-path-between-two-cities/

from typing import List
from collections import defaultdict


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        stack = []
        graph = defaultdict(list)
        visited = set()
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))
        ans = 10_001
        stack.append(1)
        while stack:
            node = stack.pop()
            for neighbor, w in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor)
                ans = min(ans, w) 
        return ans
        
n = 4
roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]

ans = Solution().minScore(n, roads)
print(ans)
