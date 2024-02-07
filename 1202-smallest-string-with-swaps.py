from typing import List
from collections import defaultdict

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        """
        get connected components of pairs, we can rearrange the connected components
        """
        n = len(s)
        groups = [0]*(n)
        graph = defaultdict(list)
        for u, v in pairs:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, count):
            if groups[node]:
                return
            groups[node] = count
            for next_node in graph[node]:
                dfs(next_node, count)

        count = 0
        for node in graph:
            if not groups[node]:
                count += 1
                dfs(node, count)

        components = defaultdict(list)
        for idx, group_id in enumerate(groups):
            if group_id != 0:
                components[group_id].append(s[idx])

        for component in components:
            components[component].sort(reverse=True)

        res = []
        for idx, group_id in enumerate(groups):
            if components[group_id]:
                ch = components[group_id].pop()
                res.append(ch)
            else:
                res.append(s[idx])
        return "".join(res)

s = "dcab"
pairs = [[0,3],[1,2],[0,2]]
ans = Solution().smallestStringWithSwaps(s, pairs)
print(ans)
        
