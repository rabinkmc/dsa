nums = [2, 4, 6, 8]
count = sum(1 if num % 2 == 0 else 0 for num in nums)
print(count)
