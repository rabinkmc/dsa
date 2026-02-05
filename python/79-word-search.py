from typing import List
from collections import deque


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        h = len(board)
        w = len(board[0])

        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(r, c, word):
            if not word:
                return True
            if r < 0 or r >= h or c < 0 or c >= w or board[r][c] != word[0]:
                return False

            temp = board[r][c]
            board[r][c] = "#"
            for dr, dc in moves:
                rr, cc = r + dr, c + dc
                if dfs(rr, cc, word[1:]):
                    board[r][c] = temp
                    return True
            board[r][c] = temp
            return False

        for i in range(h):
            for j in range(w):
                if board[i][j] == word[0]:
                    if dfs(i, j, word):
                        return True
        return False


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "SEE"
ans = Solution().exist(board, word)
assert ans == True

board = [["a", "b"]]
word = "aba"
ans = Solution().exist(board, word)
assert ans == False

board = [
    ["A", "A", "A", "A", "A", "A"],
    ["A", "A", "A", "A", "A", "A"],
    ["A", "A", "A", "A", "A", "A"],
    ["A", "A", "A", "A", "A", "A"],
    ["A", "A", "A", "A", "A", "A"],
    ["A", "A", "A", "A", "A", "A"],
]
word = "AAAAAAAAAAAABAA"
ans = Solution().exist(board, word)
assert ans == False

board = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]
# ABCE
# SFES
# ADEE
word = "ABCESEEEFS"
ans = Solution().exist(board, word)
assert ans == True

board = [["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]]
# CAA
# AAA
# BCD
word = "AAB"
ans = Solution().exist(board, word)
assert ans == True

board = [["a", "a"]]
word = "aa"
ans = Solution().exist(board, word)
assert ans == True
