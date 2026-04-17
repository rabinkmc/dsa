class Solution:
    def minOperations(self, s: str) -> int:
        # case1: assume
        # for i=0, si = 1
        # case2: assume
        # for i=0, si = 0
        case1 = 0
        case2 = 0
        s1 = [1]
        s2 = [0]
        n = len(s)

        for _ in range(n - 1):
            s1.append(1 - s1[-1])
            s2.append(1 - s2[-1])

        for i in range(n):
            case1 += int(s1[i] != int(s[i]))
            case2 += int(s2[i] != int(s[i]))

        return min(case1, case2)


s = "0100"
ans = Solution().minOperations(s)
print(ans)
