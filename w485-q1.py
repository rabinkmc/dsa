from typing import List
from collections import defaultdict, Counter
from itertools import permutations


def is_letter(ch):
    return ord("a") <= ord(ch) <= ord("z")


def is_vowel(ch):
    return ch in "aeiou"


def is_consonant(ch):
    return is_letter(ch) and not is_vowel(ch)


class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        c = 0
        v = 0
        for ch in s:
            v += int(is_vowel(ch))
            c += int(is_consonant(ch))
        print(v, c)
        if c == 0:
            return 0
        return v // c


print(Solution().vowelConsonantScore("axeyizou"))
