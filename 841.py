from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = set(rooms[0])
        for i, room in enumerate(rooms[1:], 1):
            if i not in keys:
                return False
            keys = keys | set(room)
        return True


rooms = [[1], [2], [3], []]
# rooms = [[1, 3], [3, 0, 1], [2], [0]]
print(Solution().canVisitAllRooms(rooms))
