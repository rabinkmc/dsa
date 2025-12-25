class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        license = "".join(s.split("-"))
        i = len(license)
        out = []
        prev = i
        while i > 0:
            i = max(0, i - k)
            out = [license[i:prev].upper()] + out
            prev = i
        return "-".join(out)


s = "5F3Z-2e-9-w"
k = 4
print(Solution().licenseKeyFormatting(s, k))
