# https://leetcode.com/contest/weekly-contest-326/problems/partition-string-into-substrings-with-values-at-most-k/

class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        count = 0
        right = 0
        while right < len(s):
            temp = ""
            while right < len(s) and int(temp + s[right]) <= k:
                temp = temp + s[right]
                right = right + 1
            if temp == "":
                return -1
            count = count + 1
        return count


s = "238182"
k = 5
s = "165462"
k = 60
ans = Solution().minimumPartition(s, k)
print(ans)
