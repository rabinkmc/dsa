from collections import defaultdict
from typing import List


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        event_counter = dict()
        for user, time in logs:
            if not user in event_counter:
                event_counter[user] = set()
            if not time in event_counter[user]:
                event_counter[user].add(time)
        freq_user = defaultdict(int)
        for user, items in event_counter.items():
            freq_user[user] = len(items)
        res = [0] * k
        for freq in freq_user.values():
            res[freq - 1] += 1
        return res


logs = [[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]]
k = 5
ans = Solution().findingUsersActiveMinutes(logs, k)
print(ans)
