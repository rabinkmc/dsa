class Solution:
    def compress(self, chars: list[str]) -> int:
        s = ""
        i = 0
        groups = 0
        while i < len(chars):
            to_match = chars[i]
            i = i + 1
            count = 1
            while i < len(chars) and chars[i] == to_match:
                count += 1
                i = i + 1
            if count > 1:
                s = s + to_match + str(count)
            else:
                s = s + to_match
            groups += 1
        chars = list(s)
        return groups


chars = ["a", "a", "b", "b", "c", "c", "c"]
answer = Solution().compress(chars)
print(answer)
