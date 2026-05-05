def solve_assignment(costs):
    n = len(costs)
    # memo stores (mask): min_cost
    memo = {}

    def dp(mask):
        # Base Case: All bits are 1, meaning all tasks are assigned
        if mask == (1 << n) - 1:
            return 0

        # If we've already calculated this set of tasks, return it
        if mask in memo:
            return memo[mask]

        # To determine which worker we are currently assigning:
        # We count how many bits are already set in the mask.
        # bin(mask).count('1') tells us which worker is next.
        worker_idx = bin(mask).count("1")

        res = float("inf")

        # Try assigning the current worker to every available task
        for task_idx in range(n):
            # Check if task_idx is NOT yet in the mask (is the bit 0?)
            is_present = mask & 1 << task_idx
            task_bit_set = 1 << task_idx
            if not is_present:
                # Calculate cost: current worker's cost + solve for remaining tasks
                new_mask = mask | task_bit_set
                res = min(res, costs[worker_idx][task_idx] + dp(new_mask))

        memo[mask] = res
        return res

    return dp(0)


# Example Usage:
# Worker 0: Task 0 (cost 5), Task 1 (cost 9)
# Worker 1: Task 0 (cost 1), Task 1 (cost 2)
matrix = [[5, 9], [1, 2]]

print(f"Minimum Cost: {solve_assignment(matrix)}")  # Output: 7
