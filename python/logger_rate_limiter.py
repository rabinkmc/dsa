from collections import defaultdict


class Logger:

    def __init__(self):
        self.next_ts = defaultdict(int)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        state = False
        if timestamp >= self.next_ts[message]:
            self.next_ts[message] = timestamp + 10
            state = True
        return state


# Your Logger object will be instantiated and called as such:
obj = Logger()
obj.shouldPrintMessage(1, "foo")
obj.shouldPrintMessage(2, "bar")
obj.shouldPrintMessage(3, "foo")
obj.shouldPrintMessage(8, "bar")
# obj.shouldPrintMessage(10, "foo")
# obj.shouldPrintMessage(11, "foo")
