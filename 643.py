def findMaxAverage(nums, k):
    max_sum = sum(nums[0:k])
    j = k
    for j in range(k, len(nums)):
        new_sum = max_sum + nums[j] - nums[j - k]
        max_sum = max(new_sum, max_sum)
    return max_sum / k


nums = [0, 4, 0, 3, 2]
q = [1, 12, -5, -6, 50, 3]
answer = findMaxAverage(nums, k=1)
print(answer)
