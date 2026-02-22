class Solution:
    def partitionString(self, s: str) -> int:
        counter = dict()
        n = len(s)
        i = 0
        count = 0
        ans = []
        for j in range(n):
            ch = s[j]
            counter[ch] = counter.get(ch, 0) + 1
            if counter[ch] > 1:
                counter = dict()
                counter[ch] = 1
                count += 1
                i = j
        return count + 1


s = "abacaba"
s = "ssssss"
ans = Solution().partitionString(s)
print(ans)
