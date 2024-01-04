from collections import defaultdict
from heapq import heappush
# retrieve such that key doesn't exceed the 

class TimeMap(object):

    def __init__(self):
        self.key_store = defaultdict(list)
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        heappush(self.key_store[key], (timestamp, value))

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        values = self.key_store[key]
        if timestamp < values[0][0]:
            return ""

        left = 0
        right = len(values) - 1
        index = -1
        while left <= right:
            m = (left + right) // 2
            if values[m][0] <= timestamp:
                index = m
                left = m + 1
            else:
                right = m - 1
        return values[index][1]

# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
obj.set("foo","bar",1)
assert obj.get("foo",1) == "bar"
assert obj.get("foo", 3) == "bar"
obj.set("foo", "bar2", 4)
assert obj.get("foo", 5) == "bar2"
