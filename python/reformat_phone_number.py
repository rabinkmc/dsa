class Solution:
    def reformatNumber(self, number: str) -> str:
        out = []
        i = 0
        number = number.replace("-", "").replace(" ", "")
        n = len(number)
        if n <= 3:
            return number
        out = []
        k = n
        if n % 3 == 1:
            k = n - 4
        elif n % 3 == 2:
            k = n - 2
        while i < k:
            out.append(number[i : i + 3])
            i += 3
        if k == n - 4:
            out.append(number[-4:-2])
            out.append(number[-2:])
        elif k == n - 2:
            out.append(number[-2:])
        return "-".join(out)


number = "1-23-45767"
number = "9964-"
ans = Solution().reformatNumber(number)
print(ans)
