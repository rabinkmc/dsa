from typing import List
from collections import deque


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        h = len(board)
        w = len(board[0])
        starts = deque()
        visited = set()
        for i in range(h):
            for j in range(w):
                if board[i][j] == word[0]:
                    starts.append((i, j))
        if not starts:
            return False
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for start in starts:
            visited.clear()
            stack = [(start, 1)]
            visited.add(start)
            while stack:
                (r, c), idx = stack.pop()
                if idx == len(word):
                    return True
                for dr, dc in moves:
                    rr, cc = r + dr, c + dc
                    if rr < 0 or rr >= h or cc < 0 or cc >= w:
                        continue
                    if (rr, cc) in visited:
                        continue
                    if board[rr][cc] == word[idx]:
                        stack.append(((rr, cc), idx + 1))
                        visited.add((rr, cc))
        return False

board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
#ABCE
#SFES
#ADEE
word = "ABCESEEEFS"
ans = Solution().exist(board, word)
assert ans == True

board = [["C","A","A"],["A","A","A"],["B","C","D"]]
#CAA
#AAA
#BCD
word = "AAB"
ans = Solution().exist(board, word)
assert ans == True

board = [["a", "a"]]
word = "aa"
ans = Solution().exist(board, word)
assert ans == True

board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "SEE"
ans = Solution().exist(board, word)
assert ans == True

board = [["a", "b"]]
word = "aba"
ans = Solution().exist(board, word)
assert ans == False

