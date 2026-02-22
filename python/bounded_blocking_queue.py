import threading
from collections import deque

class BoundedBlockingQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = deque()

        self.lock = threading.Lock()
        self.not_full = threading.Condition(self.lock)
        self.not_empty = threading.Condition(self.lock)

    def enqueue(self, element):
        with self.not_full:
            while len(self.queue) >= self.capacity:
                self.not_full.wait()
            self.queue.append(element)
            self.not_empty.notify()

    def dequeue(self):
        with self.not_empty:
            while len(self.queue) == 0:
                self.not_empty.wait()
            item = self.queue.popleft()
            self.not_full.notify()
            return item

    def size(self):
        with self.lock:
            return len(self.queue)

