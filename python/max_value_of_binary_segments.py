def seg_bin(segment):
    curr = 0
    for x in segment:
        curr = curr * 2 + int(x)
    return curr


class Solution:
    def maxValue(self, nums1: list[int], nums0: list[int]) -> int:
        segments = []
        for a, b in zip(nums1, nums0):
            tmp = ["1"] * a + ["0"] * b
            segments.append("".join(tmp))
        segments.sort(reverse=True)
        curr = 0
        print(segments)
        for segment in segments:
            ns = len(segment)
            curr = (curr << ns) + seg_bin(segment)
        return curr % 1_000_000_007


nums1 = [1, 2]
nums0 = [1, 0]
ans = Solution().maxValue(nums1, nums0)
print(ans)
