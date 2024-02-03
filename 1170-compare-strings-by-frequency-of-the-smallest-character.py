from typing import List



class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s):
            ch = min(s)
            return s.count(ch)

        ans = []
        for query in queries: 
            count = 0
            for word in words:
                if f(query) < f(word):
                    count += 1
            ans.append(count)
        return ans
                

        
