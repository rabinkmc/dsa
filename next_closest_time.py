class Solution:
    def nextClosestTime(self, time: str) -> str:
        hh, mm = time.split(":")
        ctime = int(hh) * 60 + int(mm)
        digits = {int(x) for x in time if x != ":"}
        combinations = []
        curr = []

        def dfs():
            if len(curr) == 4:
                combinations.append(curr[:])
                return
            for digit in digits:
                curr.append(digit)
                dfs()
                curr.pop()
        dfs()
        elapsed = 24 * 60
        for time in combinations:
            hour = time[0] * 10 + time[1]
            minute = time[2] * 10 + time[3]
            if hour >= 24 or minute >= 60:
                continue
            cur = hour * 60 + minute
            if hour < 24 and minute < 60:
                cur = hour * 60 + minute
                cand_elapsed = (cur - ctime) % (24 * 60)
                if 0 < cand_elapsed < elapsed:
                    ans = cur
                    elapsed = cand_elapsed
        return "{:02d}:{:02d}".format(*divmod(ans, 60))
ans = Solution().nextClosestTime("19:34")
print(ans)
