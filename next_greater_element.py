nums = [4, 7, 6, 3, 2, 5]

n = len(nums)
res = [-1] * n

stack = []
for i in range(n - 1, -1, -1):
    while stack and stack[-1] >= nums[i]:
        stack.pop()

    res[i] = stack[0] if stack else -1
    stack.append(nums[i])
print(res)
