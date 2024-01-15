from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.answers = []

        def get_candidates(subset, lc, rc):
            ans = []
            if lc < n:
                ans.append("(")
            if rc < lc:
                ans.append(")")
            return ans

        def backtrack(subset, lc, rc):
            if len(subset) == n * 2:
                answer = "".join(subset)
                self.answers.append(answer)
                return

            for candidate in get_candidates(subset, lc, rc):
                backtrack(
                    subset + [candidate],
                    lc + int(candidate == "("),
                    rc + int(candidate == ")"),
                )

        backtrack(["("], 1, 0)
        return self.answers


ans = Solution().generateParenthesis(3)
print(ans)
