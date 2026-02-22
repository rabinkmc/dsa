class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls_set = set()
        cows_set = set()
        for c1, c2 in zip(secret, guess):
            print(c1, c2)
            if c1 == c2:
                bulls_set.add(c1)
            else:
                cows_set.add(c2)
        bulls = len(bulls_set)
        cows = len(cows_set)


        return f"{bulls}A{cows}B"

secret, guess = "1807", "7810"
secret = "1123"
guess = "0111"
ans = Solution().getHint(secret, guess)
print(ans)
        
