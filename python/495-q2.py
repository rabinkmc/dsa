from typing import List
import heapq


class EventManager:

    def __init__(self, events: list[list[int]]):
        self.pq_events = []
        self.event_map = dict()
        for id, priority in events:
            heapq.heappush(self.pq_events, (-priority, id))
            self.event_map[id] = priority

    def updatePriority(self, eventId: int, newPriority: int) -> None:
        self.event_map[eventId] = newPriority
        heapq.heappush(self.pq_events, (-newPriority, eventId))

    def pollHighest(self) -> int:
        while self.pq_events:
            priority, event_id = heapq.heappop(self.pq_events)
            if self.event_map.get(event_id) == -priority:
                del self.event_map[event_id]
                return event_id
        return -1


events = [[5, 7], [2, 7], [9, 4]]
events = [[15, 1]]
obj = EventManager(events)

obj.updatePriority(15, 8)
obj.updatePriority(15, 4)
print(obj.event_map)
print(obj.pq_events)
print(obj.pollHighest())
print(obj.pollHighest())
