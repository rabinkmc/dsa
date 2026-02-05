subset = []
n = 3
elements = [0, 1, 2]


def search(k):
    if k == n:
        # process the subset
        print(subset)
    else:
        search(k + 1)
        subset.append(k)
        search(k + 1)
        subset.pop()


search(0)
