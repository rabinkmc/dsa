def fn(arr):
    # binary search greedy minimum
    def check(x):
        # this function is implemented depending on the problem
        return BOOLEAN


        left = MINIMUM_POSSIBLE_ANSWER
        right = MAXIMUM_POSSIBLE_ANSWER

        ans = mid
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
