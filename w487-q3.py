from typing import List
from collections import deque

def triplet(a,  b, c):
    arr = [a,b, c]
    a, b, c = sorted(arr)
    return a*a + b * b == c * c

class Solution:
    def specialNodes(self, n: int, edges: List[List[int]], x: int, y: int, z: int) -> int:
        distances = [[-1, -1, -1] for _ in range(n)]
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        X,  Y, Z = 0, 1, 2

        def bfs(start, dd):
            q = deque()
            q.append(start)
            step = 0
            visited = [False] * n
            visited[start] = True
            while q:
                q_size = len(q)
                for _ in range(q_size):
                    node = q.popleft()
                    distances[node][dd] = step
                    for adj in graph[node]:
                        if visited[adj]:
                            continue
                        q.append(adj)
                        visited[adj] = True
                step = step + 1
        bfs(x, X)
        bfs(y, Y)
        bfs(z, Z)
        ans = 0
        for dx, dy,  dz in distances:
            ans += int(triplet(dx, dy, dz))
        return ans

n = 4
edges = [[0,1],[0,2],[0,3]] 
x = 1 
y = 2
z = 3
n = 4
edges = [[0,1],[1,2],[2,3]]
x = 0
y = 3
z = 2
ans = Solution().specialNodes(n, edges, x, y, z)
print(ans)
