from typing import List

class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.r = 0
        self.c = 0
        self.vec = vec
        self.max_row = len(vec)
        

    def next(self) -> int:
        # check if we are at the ends
        while self.r < self.max_row and self.c == len(self.vec[self.r]):
            self.r = self.r + 1
            self.c = 0

        res = self.vec[self.r][self.c]
        self.c = self.c + 1
        return res
        

    def hasNext(self) -> bool:
        while self.r < self.max_row and self.c == len(self.vec[self.r]):
            self.r = self.r + 1
            self.c = 0
        return self.r < self.max_row
        


# Your Vector2D object will be instantiated and called as such:
obj = Vector2D([[1, 2, 3, 4, 5]])
