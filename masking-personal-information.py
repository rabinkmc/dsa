class Solution:
    def maskEmail(self, s):
        s = s.lower()
        name, domain = s.split("@")
        first = name[0]
        last = name[-1]
        return f"{first}*****{last}@{domain}"

    def maskNumber(self, s):
        number = []
        for ch in s:
            if ch.isdigit():
                number.append(ch)
        country_code_len = len(number) - 10
        mask = "***-***-" + "".join(number[-4:])
        if country_code_len > 0:
            return "+" + "*" * (country_code_len) + "-" + mask
        return mask

    def maskPII(self, s: str) -> str:
        if "@" in s:
            return self.maskEmail(s)

        return self.maskNumber(s)


s = "AB@qq.com"
s = "+122(234)567-890"
print(Solution().maskPII(s))
