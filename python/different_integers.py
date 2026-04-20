class Solution:
    def numDifferentIntegers(self, word: str) -> int:

        def isDigit(ch):
            return ch >= "0" and ch <= "9"

        out = []
        for ch in word:
            if not isDigit(ch):
                out.append(" ")
            else:
                out.append(ch)
        digits = {int(x) for x in "".join(out).strip().split()}
        return len(digits)


word = "a123bc34d8ef34"
ans = Solution().numDifferentIntegers(word)
print(ans)
