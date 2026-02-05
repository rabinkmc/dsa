from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        res = [0]*n
        prev = int(logs[0].split(":")[2])
        for log in logs:
            idx, status, t = log.split(":")
            idx = int(idx)
            t = int(t)
            if not stack: 
                stack.append(idx)
                continue

            if status == "start":
                res[stack[-1]] += t - prev
                stack.append(idx)
                prev = t
            else:
                top = stack.pop()
                res[top] += t - prev + 1
                prev = t + 1
        return res

n = 2
logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
print(Solution().exclusiveTime(n, logs))

