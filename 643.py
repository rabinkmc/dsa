def findMaxAverage(nums, k):
    # first calculate the sum of first k numbers
    max_sum = sum(nums[0:k])
    print(max_sum)
    print("_______________________________")
    j = k
    for j in range(k, len(nums)):
        new_sum = max_sum + nums[j] - nums[j - k]
        __import__("ipdb").set_trace()
        max_sum = max(new_sum, max_sum)
    return max_sum / k


nums = [0, 4, 0, 3, 2]
q = [1, 12, -5, -6, 50, 3]
answer = findMaxAverage(nums, k=1)
print(answer)
