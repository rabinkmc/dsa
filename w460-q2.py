class Solution:
    def numOfSubsequences(self, s: str) -> int:
        n = len(s)
        counter = [[0, 0] for _ in range(n)]
        lc, tc, cc = 0, 0, 0
        lc_count = 0
        ct_count = 0
        for i in range(n):
            lc += int(s[i] == "L")
            tc += int(s[i] == "T")
            cc += int(s[i] == "C")
            if s[i] == "C":
                lc_count += lc
            if s[i] == "T":
                ct_count += cc
            counter[i] = [lc, tc]

        if cc == 0 and lc != 0 and tc != 0:
            return lc * tc

        base, ans = 0, 0
        for i in range(n):
            if s[i] == "C":
                l = counter[i - 1][0] if i > 0 else 0
                t = tc - counter[i][1]
                base += l * t

        for i in range(n):
            if s[i] == "C":
                l = counter[i - 1][0] if i > 0 else 0
                t = tc - counter[i][1]
                ans = max(ans, base + l * t)
            else:
                l = counter[i][0]
                t = tc - counter[i][1]
                ans = max(ans, base + l * t)

        ans = max(ans, base + lc_count, base + ct_count)
        return ans


s = "LCTKLCLT"
# s = "LCLPTTGC"
ans = Solution().numOfSubsequences(s)
print(ans)
