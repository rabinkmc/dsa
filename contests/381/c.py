from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        counts = Counter(word)
        priority = list(counts.items())
        priority.sort(key = lambda x: x[1], reverse=True)
        total = 0
        for i, (_, count) in enumerate(priority):
            if i <= 7:
                total += count
            elif i <= 15:
                total += count * 2
            elif i <= 23:
                total += count * 3
            else:
                total += count * 4
        return total

word ="aabbccddeeffgghhiiiiii"
word = "xyzxyzxyzxyz"
ans = Solution().minimumPushes(word)
print(ans)

        
