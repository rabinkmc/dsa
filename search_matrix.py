from typing import List

def bsearch(row, target):
    if row[0] > target or row[-1] < target:
        return False
    l = 0
    r = len(row) - 1
    while l <= r:
        m = l + (r - l) // 2
        if row[m] == target:
            return True
        if row[m] > target:
            r = m - 1
        else:
            l = m + 1
    return False


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if bsearch(row, target):
                return True
        return False
        
