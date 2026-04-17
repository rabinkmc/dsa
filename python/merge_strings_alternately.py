class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = len(word1)
        n = len(word2)
        k = min(m, n)
        out = []
        for i in range(k):
            print(i, word1[i], word2[i])
            out.append(word1[i])
            out.append(word2[i])
        i += 1
        out.extend(word1[i:])
        out.extend(word2[i])

        return "".join(out)


word1, word2 = "abc", "pqr"
ans = Solution().mergeAlternately(word1, word2)
print(ans)
