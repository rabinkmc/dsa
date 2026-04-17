class Solution:
    def maximumTime(self, time: str) -> str:
        out = []
        hh, mm = time.split(":")
        out = [hh[0], hh[1], ":", mm[0], mm[1]]
        if out[0] == "?":
            if out[1] >= "4" and out[1] != "?":
                out[0] = "1"
            else:
                out[0] = "2"
        if out[1] == "?":
            if out[0] != "2":
                out[1] = "9"
            else:
                out[1] = "3"
        if out[3] == "?":
            out[3] = "5"
        if out[4] == "?":
            out[4] = "9"
        return "".join(out)


time = "??:?0"
ans = Solution().maximumTime(time)
print(ans)
