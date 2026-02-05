from typing import List

def valid_code(s):
    if not s:
        return False
    for ch in s:
        is_digit = ord(ch) >= ord('0') and ord(ch) <= ord('9')
        is_lowercase = ord(ch) >= ord('a') and ord(ch) <= ord('z')
        is_uppercase = ord(ch) >= ord('A') and ord(ch) <= ord('Z')
        if is_digit or is_lowercase or is_uppercase:
            continue
        else:
            return False
    return True

def valid_business(business):
    return business in ["electronics", "grocery", "pharmacy", "restaurant"]

class Solution:
    def validateCoupons(
        self, 
        code: List[str],
        businessLine: List[str],
        isActive: List[bool]
    ) -> List[str]:
        n = len(isActive)
        res = []
        for i in range(n):
            if (
                valid_code(code[i]) and 
                valid_business(businessLine[i]) and
                isActive[i]
            ):
                res.append((businessLine[i], code[i]))
        res.sort()

        return [code for _, code in res]

code = ["SAVE20","","PHARMA5","SAVE@20"]
businessLine = ["restaurant","grocery","pharmacy","restaurant"]
isActive = [True,True,True,True]
ans = Solution().validateCoupons(
    code,
    businessLine,
    isActive
)
print(ans)
