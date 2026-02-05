class Solution:
    def convert(self, s: str, numRows: int) -> str:
        output = [[] for _ in range(numRows)]
        i = 0
        while i < len(s):
            output[i % numRows].append(s[i])
            i = i + 1

        return s


s = "PAYPALISHIRING"
numRows = 3
ans = Solution().convert(s, numRows)
print(ans)
