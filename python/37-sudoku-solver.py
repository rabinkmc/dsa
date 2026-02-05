from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.cells = self.empty_cells()
        self.n = len(self.cells)
        self.solve(0)

    def solve(self, i):
        board = self.board
        if i == self.n:
            return True

        r, c = self.cells[i]
        for candidate in self.next_candidates(r, c):
            board[r][c] = candidate
            if self.solve(i+1):
                return True 
            board[r][c] = "."
        return False

    def next_candidates(self, r, c):
        board = self.board
        numbers = []
        # along the row
        for col in range(9):
            cell = board[r][col]
            if cell != ".":
                numbers.append(cell)

        for row in range(9):
            cell = board[row][c]
            if cell != ".":
                numbers.append(cell)

        i = r // 3
        j = c // 3
        for a in range(3*i, 3*i + 3):
            for b in range(3*j, 3*j + 3):
                cell = board[a][b]
                if cell != ".":
                    numbers.append(cell)
        next_candidates = []

        for i in range(1, 10):
            if str(i) not in numbers:
                next_candidates.append(str(i))
        return next_candidates

    def empty_cells(self):
        board = self.board
        empty_cells = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    empty_cells.append((i, j))
        return empty_cells


boarda = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
Solution().solveSudoku(boarda)
