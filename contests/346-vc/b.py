class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        st = list(s)
        left = 0
        right = len(st) - 1
        operations = 0

        while left < right:
            if st[left] != st[right]:
                ord_left = ord(s[left])
                ord_right = ord(s[right])
                _ord = min(ord_left, ord_right)
                operations += 1
                st[left] = chr(_ord)
                st[right] = chr(_ord)
        
            left += 1
            right -= 1
        return "".join(st)

s = "egcfe"
ans = Solution().makeSmallestPalindrome(s)
print(ans)
