def backtrack(curr, OTHER_ARGUMENTS...):
    if (BASE_CASE):
        # modify the answer
        return 
    ans = 0
    for (ITERATE_OVER_INPUT):
        # modify this current state
        ans += backtrack(curr, OTHER_ARGUMENTS...)
        # undo the modification of the current state
    return ans
