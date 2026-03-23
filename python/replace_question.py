class Solution:
    def modifyString(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return "a"
        res = list(s)
        chars = set("abcdefghijklmnopqrstuvwxyz")
        for i in range(n):
            if s[i] != "?":
                continue
            if i == 0:
                res[i] = list(chars - {res[i + 1]})[0]
            elif i == n - 1:
                res[i] = list(chars - {res[i - 1]})[0]
            else:
                res[i] = list(chars - {res[i - 1], res[i + 1]})[0]
        return "".join(res)


s = "ubv?w"
s = "j?qg??b"
ans = Solution().modifyString(s)
print(ans)
