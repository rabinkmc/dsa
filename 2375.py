class Solution:
    def smallestNumber(self, pattern: str) -> str:
        curr = []

        def get_candidates(curr, i):
            p = pattern[i]
            options = set(list(range(1, 10))) - curr
            top = curr[-1]
            candidates = []
            if p == "I":
                # select all the options that are greater than top
                for option in options:
                    if option > top:
                        candidates.append(option)
            else:
                for option in options:
                    if option < top:
                        candidates.append(option)
            return candidates

        n = len(pattern)
        ans = []

        def backtrack(i):
            if len(curr) == n + 1:
                ans.append(curr[:])
                return

            for candidate in get_canidates(curr, i):
                curr.append(candidate)
                backtrack(i + 1)
                curr.pop()

        backtrack(0)
        ans.sort()
        return ans[0]


ans = Solution().smallestNumber(pattern)
print(ans)
