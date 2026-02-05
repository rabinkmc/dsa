import heapq


class SmallestInfiniteSet:
    def __init__(self):
        self.set = list(range(1, 1000 + 1))

    def popSmallest(self) -> int:
        return heapq.heappop(self.set)

    def addBack(self, num: int) -> None:
        if num not in self.set:
            heapq.heappush(self.set, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
