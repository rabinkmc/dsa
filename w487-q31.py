from typing import List
from collections import deque


class RideSharingSystem:

    def __init__(self):
        self.drivers = deque()
        self.riders = deque()
        self.riders_idx = set()

    def addRider(self, riderId: int) -> None:
        self.riders.append(riderId)
        self.riders_idx.add(riderId)

    def addDriver(self, driverId: int) -> None:
        self.drivers.append(driverId)

    def matchDriverWithRider(self) -> List[int]:
        if self.drivers and self.riders:
            driver = self.drivers.popleft()
            rider = self.riders.popleft()
            self.riders_idx.remove(rider)
            return [driver, rider]
        return [-1, -1]

    def cancelRider(self, riderId: int) -> None:
        if riderId in self.riders_idx:
            self.riders.remove(riderId)
            self.riders_idx.remove(riderId)


# Your RideSharingSystem object will be instantiated and called as such:
obj = RideSharingSystem()
obj.addRider(3)
obj.addDriver(2)
obj.addRider(1)
param_3 = obj.matchDriverWithRider()
print(param_3)
obj.addDriver(5)
obj.cancelRider(3)
print(obj.matchDriverWithRider())
print(obj.matchDriverWithRider())
# obj.cancelRider(riderId)©leetcode
