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

def backtrack(candidate):
    if find_solution(candidate):
        output(candidate)
        return 

    for next_candidate in list_of_candidates:
        if is_valid(next_candidate):
            place(next_candidate)
            backtrack(next_candidate)
            remove(next_candidate)
