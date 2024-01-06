from typing import List

class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        acronym = [word[0] for word in words]
        return "".join(acronym) == s

print(Solution().isAcronym(words = ["alice","bob","charlie"], s = "abc"))
print(Solution().isAcronym(words = ["an","apple"], s = "a"))
print(Solution().isAcronym(words = ["never","gonna","give","up","on","you"], s = "ngguoy"))

        
