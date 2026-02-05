from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            anagrams[key].append(word)
        return list(anagrams.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
ans = Solution().groupAnagrams(strs)
print(ans)
