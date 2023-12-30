class Solution:
    def romanToInt(self, s: str) -> int:
        table = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000,
        }
        total = 0
        i = 0
        while i < len(s):
            if (i + 2) <= len(s) and s[i:i+2] in table:
                total += table[s[i:i+2]]
                i = i + 2
            elif s[i] in s:
                total += table[s[i]]
                i = i + 1
        return total


solution = Solution()
assert solution.romanToInt("III") == 3
assert solution.romanToInt("LVIII") == 58
assert solution.romanToInt("MCMXCIV") == 1994


