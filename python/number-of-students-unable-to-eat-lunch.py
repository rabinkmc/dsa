from typing import List
from collections import deque


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stds = deque(students)

        remaining = len(students)
        food = deque(sandwiches)
        visited = set()

        while stds:
            students_str = "".join(str(x) for x in stds)
            food_str = "".join(str(x) for x in food)
            if (students_str, food_str) in visited:
                return remaining
            visited.add((students_str, food_str))

            std = stds.popleft()
            if std == food[0]:
                remaining -= 1
                food.popleft()
            else:
                stds.append(std)
        return remaining


students = [1, 1, 0, 0]
sandwiches = [0, 1, 0, 1]
students = [1, 1, 1, 0, 0, 1]
sandwiches = [1, 0, 0, 0, 1, 1]
print(Solution().countStudents(students, sandwiches))
