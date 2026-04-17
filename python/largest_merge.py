class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        m = len(word1)
        n = len(word2)
        out = []
        while i < m and j < n:
            if word1[i] > word2[j]:
                out.append(word1[i])
                i += 1
            elif word2[j] > word1[i]:
                out.append(word2[j])
                j += 1
            elif word1[i:] > word2[j:]:
                out.append(word1[i])
                i += 1
            else:
                out.append(word2[j])
                j += 1

        while i < m:
            out.append(word1[i])
            i += 1
        while j < n:
            out.append(word2[j])
            j += 1

        return "".join(out)


word1, word2 = "cabaa", "bcaa"
ans = Solution().largestMerge(word1, word2)
print(ans)
