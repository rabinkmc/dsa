def permute(nums):
    res = []
    n = len(nums)
    used = [False] * n

    def backtrack(current):
        if len(current) == n:
            res.append(current[:])
            return

        for i in range(n):
            if used[i]:
                continue
            current.append(nums[i])
            used[i] = True
            backtrack(current)
            current.pop()
            used[i] = False

    backtrack([])
    print(res)


nums = [1, 2, 3]
permute(nums)
