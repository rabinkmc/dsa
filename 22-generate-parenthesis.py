from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.answers = []

        def get_candidates(subset):
            ans = []
            lc = subset.count("(")
            rc = subset.count(")")
            if lc < n:
                ans.append("(")
            if rc < lc:
                ans.append(")")
            return ans

        def backtrack(subset):
            if len(subset) == n*2:
                answer = "".join(subset)
                self.answers.append(answer)
                return 

            for candidate in get_candidates(subset):
                backtrack(subset + [candidate])

        backtrack(["("])
        print(self.answers)
ans = Solution().generateParenthesis(3)
        
