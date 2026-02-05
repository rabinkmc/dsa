import random

number = random.randint(1, 100)


def guess(n):
    if n == number:
        return 0
    if n > number:
        return -1
    return 1


def solution(n):
    lo = 0
    hi = n + 1
    while True:
        mid = (hi + lo) // 2
        print(lo, mid, hi)
        if guess(mid) == 0:
            print("guess was: ", number)
            print("answer: ", mid)
            return mid
        elif guess(mid) == -1:
            hi = mid
        else:
            lo = mid


solution(100)
