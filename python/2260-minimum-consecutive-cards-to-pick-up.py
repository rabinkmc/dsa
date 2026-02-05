from typing import List


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        window = {}
        n = len(cards)
        i = 0
        res = n + 1
        for j in range(n):
            x = cards[j]
            window[x] = window.get(x, 0) + 1
            while window[x] == 2:
                length = j - i + 1
                res = min(res, length)
                icard = cards[i]
                window[icard] -= 1
                i += 1

        if res == n + 1:
            return -1

        return res


cards = [3, 4, 2, 3, 4, 7]
cards = [1, 0, 5, 3, 3]
ans = Solution().minimumCardPickup(cards)
print()
print(ans)
