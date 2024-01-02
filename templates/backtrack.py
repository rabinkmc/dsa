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
    
    # iterate all possible candidates.
    for next_candidate in list_of_candidates:
        if is_valid(next_candidate):
            # try this partial candidate solution
            place(next_candidate)
            # given the candidate, explore further.
            backtrack(next_candidate)
            # backtrack
            remove(next_candidate)
"""
Backtracking is a general algorithm for finding all(or some) solutions
to some computational problems (constraint satisfaction problem) which 
incrementally builds candidates to the solution and abandons a candidate
as soon as it determines that the candidate cannot to lead to a valid
solution

Here are a few notes about the above pseudocode.

1. Overall, the enumeration of candidates is done in two levels: 1). at the
first level, the function is implemented as recursion. At each occurrence of
recursion, the function is one step further to the final solution.  2). as the
second level, within the recursion, we have an iteration that allows us to
explore all the candidates that are of the same progress to the final solution.

2. The backtracking should happen at the level of the iteration within the
recursion. 

3. Unlike brute-force search, in backtracking algorithms we are often able to
determine if a partial solution candidate is worth exploring further 
(i.e. is_valid(next_candidate)),
which allows us to prune the search zones. This is also known as the constraint,
e.g. the attacking zone of queen in N-queen game. 

4. There are two symmetric functions that allow us to mark the decision
(place(candidate)) and revert the decision (remove(candidate)).  
"""
