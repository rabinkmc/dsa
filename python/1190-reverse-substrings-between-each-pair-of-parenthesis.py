# https://leetcode.com/contest/weekly-contest-154/problems/reverse-substrings-between-each-pair-of-parentheses/

class Solution:
    def reverseParentheses(self, s: str) -> str:
        result = []
        for ch in s:
            if ch != ")":
                result.append(ch)
            else: 
                temp = []
                while result[-1] != "(":
                    temp.append(result.pop())
                result.pop()
                result.extend(temp)
        return "".join(result)

s = "(ed(et(oc))el)"
ans = Solution().reverseParentheses(s)
print(ans)

                    






        
