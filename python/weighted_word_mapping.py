from typing import List

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        def get_char(word):
            total = 0
            for ch in word:
                idx = ord(ch) - ord('a')
                total += weights[idx]
            total = 25 - total % 26 
            return chr(ord('a') + (total % 26))

        out = []
        for word in words:
            out.append(get_char(word))
        return "".join(out)


words = ["abcd","def","xyz"]
words = ["abcd"]
weights = [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]
ans = Solution().mapWordWeights(words, weights)
print(ans)
        
