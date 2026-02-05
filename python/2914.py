class Solution:
    def minChanges(self, s: str) -> int:
        length = len(s)
        factors = []
        for i in range(2, length + 1):
            if length % i == 0 and i % 2 == 0:
                factors.append(i)

        ans = float('inf')
        for factor in factors:
            total = 0
            for i in range(0, length, factor):
                partition = s[i:i+factor]
                to_zero_count = sum(ch != "0" for ch in partition)
                to_one_count = sum(ch != "1" for ch in partition)
                min_changes = min(to_zero_count, to_one_count)
                total += min_changes
            if total == 0:
                return 0
            ans = min(ans, total)

        return ans


s = "1001"
s = "111111111110010001"
ans = Solution().minChanges(s)
print(ans)
