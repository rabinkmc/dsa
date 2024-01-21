"""
for i, x in enumerate(arr):
    while stack and arr[stack[-1]] >= x:
        stack.pop()
    if stack:
        left[i] = stack[-1]
    stack.append(i)

stack = []
for i in range(n-1, -1, -1):
    while stack and arr[stack[-1]] > arr[i]:
        stack.pop()
    if stack:
        right[i] = stack[-1]
    stack.append(i)
"""
def fn(arr):
    stack = []
    ans = 0

    for num in arr:
        # for monotonic decreasing, just flip the > to <
        while stack and stack[-1] > num:
            # do logic
            stack.pop()
        stack.append(num)
    return ans
