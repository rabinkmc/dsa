from typing import List

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False]*n

        stack = [0]
        ans = 0
        rest = set(restricted)
        visited[0] = True
        while stack:
            node = stack.pop()
            print(node)
            ans += 1
            for adj in graph[node]:
                if not visited[adj] and not (adj in rest):
                    visited[adj] = True
                    stack.append(adj)
        return ans

n = 7
edges = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]]
restricted = [4,5]
# n = 7
# edges = [[0,1],[0,2],[0,5],[0,4],[3,2],[6,5]]
# restricted = [4,2,1]
ans = Solution().reachableNodes(n, edges, restricted)
print("ans:", ans)
