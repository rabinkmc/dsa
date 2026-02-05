from typing import List
from heapq import heappush, heappop

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.pq = []
        self.k = k
        for num in nums:
            heappush(self.pq, num)
            if len(self.pq) > self.k:
                heappop(self.pq)

    def add(self, val: int) -> int:
        heappush(self.pq, val)
        if len(self.pq) > self.k:
            heappop(self.pq)
        return self.pq[0]
        


# Your KthLargest object will be instantiated and called as such:
k = 3
nums = [4, 5, 8, 2]
obj = KthLargest(k, nums)
print(obj.add(6))
print(obj.add(7))
print(obj.add(8))
