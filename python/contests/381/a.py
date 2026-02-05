class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(set(word))
        cost = 0
        if n > 24: 
            rem = n - 24 
            cost += rem * 4 + 3*8 + 2*8 + 1*8 
            return cost
        if n > 16: 
            rem = n - 16
            cost += rem*3 + 2*8 + 1*8
            return cost
        if n > 8: 
            rem = n - 8
            cost += rem*2 + 1*8
            return cost
        return n 

word = "xycdefghij"
ans = Solution().minimumPushes(word)
print(ans)

        
