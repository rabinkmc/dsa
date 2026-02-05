from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            graph[v].append(u)

        UNVISITED, VISITING, VISITED = 0, 1, 2
        n = len(graph)
        state = [UNVISITED] * n

        def has_cycle(course):
            if state[course] == VISITED:
               return False
            if state[course] == VISITING:
                return True
            state[course] = VISITING
            for neighbor in graph[course]:
                if has_cycle(neighbor):
                    return True
            state[course] = VISITED
            return False

        for course in range(n):
            if state[course] == UNVISITED and has_cycle(course):
                return False
        return True


solution = Solution().canFinish(numCourses=2, prerequisites=[[1, 0]])
assert solution == True
solution = Solution().canFinish(numCourses=2, prerequisites=[[1, 0], [0, 1]])
assert solution == False, solution
solution = Solution().canFinish(numCourses=4, prerequisites=[[1, 0], [2, 1], [0, 2]])
assert solution == False, solution
