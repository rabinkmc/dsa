class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        counter = [0] * 26

        j = 0
        i = 0
        ans = 0

        def check():
            peak = 0
            total = 0
            for count in counter:
                peak = max(peak, count)
                total += count
            return total - peak <= k

        while j < n:
            idx = ord(s[j]) - ord("A")
            counter[idx] += 1
            while not check():
                idx = ord(s[i]) - ord("A")
                counter[idx] -= 1
                i = i + 1
            ans = max(ans, j - i + 1)
            j = j + 1

        return ans


# s = "ABAB"
# k = 2
s = "AABABBA"
k = 1
print(Solution().characterReplacement(s, k))
