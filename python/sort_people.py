from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        items = list(zip(heights, names))
        items.sort(key=lambda x: -x[0])
        return [x[1] for x in items]


ans = Solution().sortPeople(names, heights)
