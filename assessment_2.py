class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        j = 0
        n1, n2 = len(name), len(typed)
        while i < n1 and j < n2:
            if name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j - 1] and typed[j] == name[i - 1]:
                j += 1
            else:
                return False
        if i < n1:
            return False
        while j < n2:
            if typed[j] != typed[j - 1]:
                return False
            j += 1

        return True


name = "zlexya"
typed = "aazlllllllllllllllleexxxya"

# name = "saeed"
# typed = "ssaaedd"
ans = Solution().isLongPressedName(name, typed)
print(ans)
