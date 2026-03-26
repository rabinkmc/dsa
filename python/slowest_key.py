from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        slowest = keysPressed[0]
        max_duration = releaseTimes[0]
        for i in range(1, len(releaseTimes)):
            diff = releaseTimes[i] - releaseTimes[i - 1]
            ch = keysPressed[i]
            if diff > max_duration or (diff == max_duration and ch > slowest):
                slowest = ch
                max_duration = diff
        return slowest


releaseTimes = [9, 29, 49, 50]
keysPressed = "cbcd"
ans = Solution().slowestKey(releaseTimes, keysPressed)
print(ans)
