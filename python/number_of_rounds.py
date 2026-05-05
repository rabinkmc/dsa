class Timer:
    def __init__(self, time):
        hh, min = time.split(":")
        self.hh = int(hh)
        self.min = int(min)
        self.time = self.hh * 60 + self.min


class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        t1 = Timer(loginTime)
        t2 = Timer(logoutTime)

        def upper_clamp(min):
            if min in [0, 15, 30, 45]:
                return 0
            if min > 45:
                return 60 - min
            elif min > 30:
                return 45 - min
            elif min > 15:
                return 30 - min
            else:
                return 15 - min

        def lower_clamp(min):
            if min in [0, 15, 30, 45]:
                return 0
            if min < 15:
                return min
            elif min < 30:
                return min - 15
            elif min < 45:
                return min - 30
            else:
                return min - 45

        d1 = upper_clamp(t1.min)
        d2 = lower_clamp(t2.min)
        if t2.hh > t1.hh or (t2.hh == t1.hh and t2.min > t1.min):
            return min(0, (t2.time - t1.time - d1 - d2) // 15)
        else:
            return min(0, (24 * 60 - (t1.time - t2.time) - d1 - d2) // 15)


loginTime = "09:31"
logoutTime = "10:14"
loginTime = "21:31"
logoutTime = "03:00"
loginTime = "06:13"
logoutTime = "06:19"
loginTime = "00:47"
logoutTime = "00:57"

ans = Solution().numberOfRounds(loginTime, logoutTime)
print(ans)
