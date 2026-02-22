import random


class RandomizedSet:

    def __init__(self):
        self.hashmap = dict()
        self.nodes = []

    def insert(self, val: int) -> bool:
        if val in self.hashmap:
            return False
        self.nodes.append(val)
        self.hashmap[val] = len(self.nodes) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hashmap:
            return False
        idx = self.hashmap[val]
        last = len(self.nodes) - 1
        self.hashmap[self.nodes[-1]] = idx
        if idx != last:
            self.nodes[idx], self.nodes[last] = self.nodes[last], self.nodes[idx]
        del self.hashmap[val]
        self.nodes.pop()
        return True

    def getRandom(self) -> int:
        return random.choices(self.nodes)[0]


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
obj.insert(51)
obj.insert(2)
obj.insert(10)
obj.remove(51)
print(obj.hashmap, obj.nodes)
param_3 = obj.getRandom()
print(param_3)
