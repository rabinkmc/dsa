from collections import Counter
class Solution:
    def maximumXor(self, s: str, t: str) -> str:
        tc = Counter(t)
        t0 = tc['0']
        t1 = tc['1']
        ans = []
        for c1 in s:
            bit = '0'
            if t0 > 0 and c1 == '1':
                t0 = t0 - 1
                bit = '1'
            if t1 > 0 and c1 == '0':
                t1 = t1  - 1
                bit = '1'
            ans.append(bit)
        return "".join(ans)

s = "0101"
t = "1001"
ans = Solution().maximumXor(s,t)
print(ans)
