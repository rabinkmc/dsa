from typing import List


class OrderedStream:

    def __init__(self, n: int):
        self.streams = [""] * n
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.streams[idKey - 1] = value
        if idKey - 1 != self.ptr:
            return []

        self.ptr += 1
        result = []
        while self.ptr < len(self.streams) and self.streams[self.ptr]:
            result.append(self.streams[self.ptr])
            self.ptr += 1
        return result


# Your OrderedStream object will be instantiated and called as such:
obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
