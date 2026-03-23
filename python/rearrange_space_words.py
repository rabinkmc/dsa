class Solution:
    def reorderSpaces(self, text: str) -> str:
        space_sz = 0
        for ch in text:
            if ch == " ":
                space_sz += 1
        words = text.strip().split()
        if len(words) == 1:
            return words[0] + " " * space_sz
        spacer = space_sz // (len(words) - 1)
        end_space = space_sz % (len(words) - 1)
        joiner = " " * spacer
        res = joiner.join(words)
        res = res + " " * end_space
        return res


text = "  this   is  a sentence "
ans = Solution().reorderSpaces(text)
print(ans)
