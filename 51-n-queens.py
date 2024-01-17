from typing import List

class Chess:
    def __init__(self, n):
        self.n = n
        self.diag1, self.diag2 = self.get_diagonals()
        self.board = self.construct_board()
        self.answer = []

    def construct_board(self):
        board = []
        n = self.n
        for _ in range(n):
            temp = []
            for _ in range(n):
                temp.append(".")
            board.append(temp)
        return board

    def get_diagonals(self):
        diag = []
        n = self.n
        for i in range(n):
            temp = []
            for j in range(i, i + n):
                temp.append(j)
            diag.append(temp)
        return diag, diag[::-1]

    def not_safe(self, r1, c1, r2, c2):
        diag1 = self.diag1
        diag2 = self.diag2
        if r1 == r2 or c1 == c2:
            return True
        if diag1[r1][c1] == diag1[r2][c2]:
            return True
        if diag2[r1][c1] == diag2[r2][c2]:
            return True
        return False

    def place_queens(self, candidates):
        board = self.construct_board()
        for r, c in candidates:
            board[r][c] = 'Q'
        output = []
        for row in board:
            output.append("".join(row))
        return output

    def next_candidates(self, r1, candidates):
        nxt_canidates = []
        for c1 in range(self.n):
            for r2, c2 in candidates: 
                if self.not_safe(r1,c1, r2, c2):
                    break
            else:
                nxt_canidates.append((r1, c1))
        return nxt_canidates

    def solve(self, cur_row, candidates):
        if len(candidates) == self.n:
            board = self.place_queens(candidates)
            self.answer.append(board)
            return

        for candidate in self.next_candidates(cur_row, candidates):
            candidates.append(candidate)
            self.solve(cur_row + 1, candidates)
            candidates.pop()

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        chess = Chess(n)
        chess.solve(0, [])
        return chess.answer


ans = Solution().solveNQueens(4)
print(ans)
        
