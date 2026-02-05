from collections import deque


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = dict()
        self.items = deque()

    def __str__(self):
        return str(self.dict)

    def get(self, key: int) -> int:
        if key in self.dict:
            return self.dict[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict[key] = value
            return
        # new key
        if len(self.items) >= self.capacity:
            lru_key = self.items.popleft()
            del self.dict[lru_key]
        self.items.append(key)
        self.dict[key] = value


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(1, 1)
obj.put(2, 2)
print(obj.get(1))
obj.put(3, 3)
print(obj.get(2))
obj.put(4, 4)
