# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:
import collections

from typing import List

class Solution:
    def __init__(self):
        self.buffer = collections.deque()

    def read(self, buf: List[str], n: int) -> int:
        rc = 0

