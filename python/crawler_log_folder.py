from typing import List

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ops = 0
        for log in logs:
            if log == "./":
                continue
            if log == "../":
                ops -= 1
            else:
                ops += 1
        return ops

logs = ["d1/","d2/","./","d3/","../","d31/"]
ans = Solution().minOperations(logs)
print(ans)
