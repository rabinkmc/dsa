from typing import List
from collections import defaultdict

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losers = defaultdict(int)
        players = set()
        no_losses = []
        one_loss = []
        for winner, loser in matches:
            losers[loser] += 1
            players.add(loser)
            players.add(winner)
        for player in players:
            if losers[player] == 0:
                no_losses.append(player)
            elif losers[player] == 1:
                one_loss.append(player)
        no_losses.sort()
        one_loss.sort()
        return [no_losses, one_loss]

matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
matches = [[2,3],[1,3],[5,4],[6,4]]
ans = Solution().findWinners(matches)
print(ans)

