# https://leetcode.com/contest/weekly-contest-327/problems/make-number-of-distinct-characters-equal/
from collections import Counter

class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        # check if there is a brute force solution
        # can you do the simulation
        # in this case we can just swap two keys
        # and check their count
        c1 = Counter(word1)
        c2 = Counter(word2)
        c1k = list(c1.keys())
        c2k = list(c2.keys())
        m = len(c1)
        n = len(c2)
        for k1 in c1k:
            for k2 in c2k:
                # now swap k1 and k2 keys
                # when I swap them, I reduce the count in one and increase in another
                # after swapping check if there are same number of keys
                # swapping k1 and k2
                c1[k1] -= 1
                c2[k1] += 1
                c2[k2] -= 1
                c1[k2] += 1

                if c1[k1] == 0:
                    del c1[k1]

                if c2[k2] == 0:
                    del c2[k2]

                if len(c1) == len(c2):
                    return True

                c1[k1] += 1
                c2[k1] -= 1
                c2[k2] += 1
                c1[k2] -= 1

                if c2[k1] == 0:
                    del c2[k1]

                if c1[k2] == 0:
                    del c1[k2]

        return False



ans = Solution().isItPossible(word1 = "aab", word2 = "bccd")
print(ans)
