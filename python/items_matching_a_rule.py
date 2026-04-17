from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        rule = {"type": 0, "color": 1, "name": 2}[ruleKey]
        count = 0
        for item in items:
            count += int(item[rule] == ruleValue)
        return count


items = [
    ["phone", "blue", "pixel"],
    ["computer", "silver", "lenovo"],
    ["phone", "gold", "iphone"],
]
ruleKey = "color"
ruleValue = "silver"
ans = Solution().countMatches(items, ruleKey, ruleValue)
print(ans)
