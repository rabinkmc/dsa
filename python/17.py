from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def helper(digits):
            if len(digits) == 1:
                return list(self.get_letters(digits))
            digit = digits[0]
            answer = []
            for letter in self.get_letters(digit):
                answer.extend([letter + c for c in helper(digits[1:])])
            return answer

        return helper(digits)

    def get_letters(self, digit):
        return {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }[digit]


print(Solution().letterCombinations("234"))
