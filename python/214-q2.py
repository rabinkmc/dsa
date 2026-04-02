from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        counter = Counter(s)
        items = sorted(counter.values(), reverse=True)
        n = len(items)
        cost = 0
        for i in range(1, n):
            if items[i - 1] == 0:
                return cost + sum(items[i:])
            if items[i] < items[i - 1]:
                continue
            if items[i] == items[i - 1]:
                items[i] = items[i] - 1
                cost += 1
            else:
                cost += items[i] - items[i - 1] + 1
                items[i] = items[i - 1] - 1
        return cost


s = "aaabbbcc"
# s = "ceabaacb"
s = "abcabc"
# s = "bbbbace"
ans = Solution().minDeletions(s)
print(ans)
