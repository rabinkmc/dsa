class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        counter = {"a": 0, "b": 0, "c": 0}
        for ch in s:
            if ch not in "abc":
                continue
            counter[ch] += 1

        for ch in "abc":
            if counter[ch] < k:
                return -1
        i = 0
        max_window = 0
        window = {"a": 0, "b": 0, "c": 0}

        def valid():
            case1 = counter["a"] - window["a"] >= k
            case2 = counter["b"] - window["b"] >= k
            case3 = counter["c"] - window["c"] >= k
            return case1 and case2 and case3

        def invalid():
            case1 = counter["a"] - window["a"] < k
            case2 = counter["b"] - window["b"] < k
            case3 = counter["c"] - window["c"] < k
            return case1 or case2 or case3

        for j in range(len(s)):
            ch = s[j]
            if ch not in "abc":
                continue
            window[ch] += 1
            # check out window is valid
            # to check out window is valid
            if valid():
                max_window = max(max_window, j - i + 1)

            while invalid():
                ci = s[i]
                window[ci] -= 1
                i += 1

        return len(s) - max_window


s = "aabaaaacaabc"
k = 2
ans = Solution().takeCharacters(s, k)
print(ans)
