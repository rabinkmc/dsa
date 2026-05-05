from typing import List


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        years = 2050 - 1950 + 1
        deaths = [0] * years
        births = [0] * years
        for birth_year, death_year in logs:
            births[birth_year - 1950] += 1
            deaths[death_year - 1950] += 1
        max_population = -1
        population = [0] * years
        population[0] = births[0] - deaths[0]
        for i in range(1, years):
            population[i] = population[i - 1] + births[i] - deaths[i]

        max_population = max(population)
        for i in range(years):
            if population[i] == max_population:
                return i + 1950
        return -1


logs = [[1993, 1999], [2000, 2010]]
ans = Solution().maximumPopulation(logs)
print(ans)
