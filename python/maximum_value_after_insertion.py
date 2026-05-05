class Solution:
    def maxValue(self, n: str, x: int) -> str:
        out = []
        target = str(x)
        if n[0] == "-":
            out = ["-"]
            i = 1
            while i < len(n) and n[i] < target:
                out.append(n[i])
                i += 1
            out.append(target)
            return "".join(out) + n[i:]
        else:
            print("here")
            i = 0
            while i < len(n) and n[i] > target:
                out.append(n[i])
                i += 1
            out.append(target)
            return "".join(out) + n[i:]


n = "-875"
x = 6
ans = Solution().maxValue(n, x)
print(ans)
