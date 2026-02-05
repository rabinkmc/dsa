# https://leetcode.com/contest/weekly-contest-322/problems/divide-players-into-teams-of-equal-skill/
"""
s = find total sum
n = no of pairs
total sum % n == 0  else return -1 (no sum exists)

1 10 12 13
s = 1 + 10 + 12 + 13 = 36 (9)
n = 2
so the sum

[3,2,5,1,3,4]

3: 2
2: 1
4: 1
1: 1
5: 1

Condition all(count(num) % 2 == 0 if num * 2 == sum else count(num) == count(complement of num))


so the sum of pairs is s // n, in this case it is 18
so the count of any number and its complement sum has to be equal else return -1
so, all the numbers have to be less than 9 in order to form sum
"""
from typing import List
from collections import Counter

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        S = sum(skill)
        n = len(skill) // 2 # no of pairs
        if S % n != 0:
            return -1

        target = S // n
        # now check the condition
        counter = Counter(skill)
        half = target % 2 == 0 and target // 2

        if half and half in counter:
            if counter[half] % 2 != 0:
                return -1
        pair_sum = (counter[half] // 2) * ( half * half) 
        del counter[half]

        visited = set()
        for num in counter:
            if num in visited:
                continue
            if counter[num] != counter.get(target-num, -1): 
                return -1

            visited.add(target-num)
            pair_sum += counter[num] * ( num * (target - num))
        return pair_sum

skill = [3,2,5,1,3,4]
skill = [3, 4]
ans = Solution().dividePlayers(skill) 
print(ans)
