from typing import List

class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        counts = set()
        for bulb in bulbs:
            if bulb in counts:
                counts.remove(bulb)
            else:
                counts.add(bulb)
        ans = list(counts)
        ans.sort()
        return ans
