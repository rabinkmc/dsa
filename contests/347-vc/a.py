class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        j = len(num) - 1
        while num[j] == "0": 
            j = j - 1
        return num[:j+1]

num = "1000"
num = "1230000"
print(Solution().removeTrailingZeros(num))
