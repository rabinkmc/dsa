abcd = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
abcd.append(0)


def min_cost(cost):
    if not cost:
        return 0
    if len(cost) <= 2:
        return min(cost)
    a = cost[0] + min_cost(cost[2:])
    b = cost[0] + min_cost(cost[1:])
    answers = min(a, b)
    return answers


print(min_cost(abcd))
