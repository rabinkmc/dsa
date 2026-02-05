# https://leetcode.com/contest/weekly-contest-322/problems/circular-sentence/

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        n = len(words)
        for i in range(n):
            cword = words[i]
            nword = words[(i+1)%n]
            if cword[-1] != nword[0]:
                return False
        return True


sentence = "eetcode"
ans = Solution().isCircularSentence(sentence)
        
