class Solution:
    def smallestString(self, s: str) -> str:
        if all(ch == "a" for ch in s):
            return s[0:-1] + "z"
        i = 0 
        res = []
        n = len(s)
        while i < n and s[i] == "a":
            res.append(s[i])
            i = i + 1
        while i < n and s[i] != "a":
            ch = chr(ord(s[i]) - 1)
            res.append(ch)
            i = i + 1
        while i < n: 
            res.append(s[i])
            i = i + 1
        return "".join(res)
        
ans = Solution().smallestString("a")
print(ans)
        
