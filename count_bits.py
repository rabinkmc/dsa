def countBits(n: int) -> list[int]:
    answer = []
    # for i in range(n + 1):
    count = 0
    i = n
    while i:
        print(i)
        one_bit = i & 1
        print(one_bit)
        count = count + one_bit
        i = i >> 1
        print(i)
    answer.append(count)
    return answer


print(countBits(3))
