from typing import List
# I was serially visiting the rooms, that doesn't work
# I can go to room 2 and then go to room 1 as well

# what's the idea
# idea is to go to the first room, collect all the keys from that room
# now go to all the room that I have keys to, and collect the keys from there
# At the end check if you have all the keys


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = [0]
        rooms_visited = set()
        while stack:
            cur = stack.pop()
            if cur in rooms_visited:
                continue
            rooms_visited.add(cur)
            stack.extend(rooms[cur])
        rooms_visited.add(0)
        return len(rooms_visited) == len(rooms)


rooms = [[1], [2], [3], []]
rooms = [[1, 3], [3, 0, 1], [2], [0]]
print(Solution().canVisitAllRooms(rooms))
