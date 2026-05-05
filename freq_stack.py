from collections import defaultdict


class FreqStack:

    def __init__(self):
        self.counter = dict()
        self.max_freq = 0
        self.group = defaultdict(list)

    def push(self, val: int) -> None:
        self.counter[val] = self.counter.get(val, 0) + 1
        count = self.counter[val]
        self.group[count].append(val)
        if count > self.max_freq:
            self.max_freq = count

    def pop(self) -> int:
        top = self.group[self.max_freq].pop()
        self.counter[top] -= 1
        if not self.group[self.max_freq]:
            self.max_freq -= 1
        return top


obj = FreqStack()
obj.push(5)
obj.push(5)
obj.push(5)
obj.push(5)
obj.push(7)
obj.push(7)
obj.push(2)
for _ in range(7):
    print(obj.pop())
