from collections import deque

class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        queue = deque([x])
        count = 0
        visited = set()
        while queue:
            qs = len(queue)
            for _ in range(qs):
                node = queue.popleft()
                if node in visited:
                    continue
                if node == y:
                    return count
                visited.add(node)
                if node % 5 == 0:
                    queue.append(node//5)
                if node % 11 == 0:
                    queue.append(node//11)
                queue.append(node - 1)
                queue.append(node + 1)

            count += 1
        return count

ans = Solution().minimumOperationsToMakeEqual(1,19) 
print(ans)
