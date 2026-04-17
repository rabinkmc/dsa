from typing import List
from collections import Counter

targets = []
cprod = 1
for _ in range(22):
    cprod = cprod * 2
    targets.append(cprod)


class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        counter = Counter(deliciousness)
        ans = 0
        seen = set()
        for key in counter:
            for target in targets:
                rem = target - key
                if (key, rem) in seen or (rem, key) in seen:
                    continue
                if rem in counter:
                    if rem == key:
                        ans += (counter[key] * (counter[key] - 1)) // 2
                    else:
                        ans += counter[key] * counter[rem]
                    seen.add((key, rem))
        return ans


deliciousness = [1, 3, 5, 7, 9]
ans = Solution().countPairs(deliciousness)
print(ans)
