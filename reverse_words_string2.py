from typing import List

def reverseWords(s,left,right):
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        reverseWords(s, 0, n-1)
        i = 0
        start = 0
        while i < n:
            while i < n and s[i] != " ":
                i += 1

            reverseWords(s, start, i-1)
            start = i + 1
            i += 1

s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
ans = Solution().reverseWords(s)
print(ans)
        
