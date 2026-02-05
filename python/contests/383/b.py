class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        """
        you don't have to worry about the characters that you append at the end just assume them to be the wildcard
        """
        step = 1
        while True:
            suffix = word[k*step:]
            if word.startswith(suffix):
                return step
            step += 1
        
word = "ab"
k = 2

word = "abcbabcd"
k = 2
print(Solution().minimumTimeToInitialState(word, k))
