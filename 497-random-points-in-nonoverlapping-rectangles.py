import random
from typing import List


class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.weights = []
        for x1, y1, x2, y2 in rects:
            self.weights.append((x2 - x1 + 1) * (y2 - y1 + 1))

    def pick(self) -> List[int]:
        x1, y1, x2, y2 = random.choices(self.rects, weights=self.weights, k=1)[0]
        return [random.randint(x1, x2), random.randint(y1, y2)]


rects = [[-2, -2, 1, 1], [2, 2, 4, 6]]
# Your Solution object will be instantiated and called as such:
obj = Solution(rects)
# param_1 = obj.pick()
