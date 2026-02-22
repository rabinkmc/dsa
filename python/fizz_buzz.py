from typing import List


def fizzBuzzer(i):
    if i % 3 == 0 and i % 5 == 0:
        return "FizzBuzz"
    if i % 3 == 0:
        return "Fizz"
    if i % 5 == 0:
        return "Buzz"
    return str(i)


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        out = []
        for i in range(1, n + 1):
            out.append(fizzBuzzer(i))
        return out
