from typing import List

class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        ls = list(s)
        hashmap = dict(zip(sources, targets))
        for i in range(indices[0], indices[1]):
            if ls[i] in hashmap:
                ls[i] = hashmap[ls[i]]
        return "".join(ls)

