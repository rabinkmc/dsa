class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        return dp[m][n]


text1 = "abcde"
text2 = "ace"

# if both last character are same
# we know we have a subsequence of at least one
# now we can process the remaining characters
# suppose the last chracters aren't same
# we find the longest prefix  of either abcde with ac or abcd with ace
#
"""
                                        (abcde, ace)

                          (abcde, ac)                          (abcd, ace)

                (abcde, a)          (abcd, ac)            (abcd, ac)             (abc, ace)

            (abcde, ) (abcd, a) (abcd, a) (abc, ac)    (abc, ac) (abc, ac)     (abc, ac)  (ab,ace)
"""


"""
dp[i][j] is the lcs of first i characters of text1 and first j characters of text2
   "" a b c d e
"" 0  0 0 0 0 0 
a  0  1 1 1 1 1 
c  0  0 0
e  0

"""

print(Solution().longestCommonSubsequence(text1, text2))
