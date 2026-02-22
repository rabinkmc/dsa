def is_char(ch):
    return ord('a') <= ord(ch) <= ord('z')

class Solution:
    def reverseByType(self, s: str) -> str:
        letters = []
        specials = []
        for ch in s:
            if is_char(ch):
                letters.append(ch)
            else:
                specials.append(ch)
        out = []
        for ch in s:
            if is_char(ch):
                out.append(letters.pop())
            else:
                out.append(specials.pop())
        return "".join(out)

s = ")ebc#da@f("
ans = Solution().reverseByType(s)
print(ans)
