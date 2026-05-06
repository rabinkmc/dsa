from heapq import heappush, heappop


class AuctionSystem:

    def __init__(self):
        self.items = dict()
        self.bidders = dict()

    def addBid(self, userId: int, itemId: int, bidAmount: int) -> None:
        if itemId not in self.items:
            self.items[itemId] = []
        if itemId not in self.bidders:
            self.bidders[itemId] = dict()

        heappush(self.items[itemId], (-bidAmount, -userId))
        self.bidders[itemId][userId] = bidAmount

    def updateBid(self, userId: int, itemId: int, newAmount: int) -> None:
        self.bidders[itemId][userId] = newAmount
        heappush(self.items[itemId], (-newAmount, -userId))

    def removeBid(self, userId: int, itemId: int) -> None:
        del self.bidders[itemId][userId]

    def getHighestBidder(self, itemId: int) -> int:
        while itemId in self.items and self.items[itemId]:
            bidAmount, userId = self.items[itemId][0]
            if userId not in self.bidders.get(itemId, {}) or (
                self.bidders[itemId][userId] != -bidAmount
            ):
                heappop(self.items[itemId])
            else:
                return userId
        else:
            return -1


# Your AuctionSystem object will be instantiated and called as such:
obj = AuctionSystem()
obj.addBid(1, 7, 5)
obj.addBid(2, 7, 6)
print(obj.getHighestBidder(7))
obj.updateBid(1, 7, 7)
print(obj.getHighestBidder(7))
obj.addBid(3, 7, 8)
print(obj.getHighestBidder(7))
obj.removeBid(3, 7)
print(obj.getHighestBidder(7))
obj.removeBid(1, 7)
print(obj.getHighestBidder(7))
# obj.updateBid(userId,itemId,newAmount)
# obj.removeBid(userId,itemId)
# param_4 = obj.getHighestBidder(itemId)
