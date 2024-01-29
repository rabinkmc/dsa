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
        m = len(c1)
        n = len(c2)
        for k1 in c1:
            for k2 in c2:
                # now swap k1 and k2 keys
                # when I swap them, I reduce the count in one and increase in another
                # after swapping check if there are same number of keys
                # swapping k1 and k2
                t1, t2 = m, n
                print(k1, k2, m, n, c1[k1], c2[k2])
                if c1[k1] == 1:
                    m = m - 1
                if k2 not in c1:
                    m = m + 1
                if c2[k2] == 1:
                   n = n - 1
                if k1 not in c2:
                    n = n + 1
                print(k1, k2, m, n, c1[k1], c2[k2])
                if m == n:
                   return True
                m, n = t1, t2

        return False


ans = Solution().isItPossible(word1="aa", word2="ab")
print(ans)
