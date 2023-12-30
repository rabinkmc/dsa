from typing import List
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        zeros = []
        h = len(mat)
        w = len(mat[0])
        #get initial nodes with item zero
        queue = deque() 
        for i in range(h):
            for j in range(w):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = -1 # track unvisited nodes
        count = 0
        moves = [(-1, 0), (1, 0), (0,-1), (0, 1)]
        while queue:
            r, c = queue.popleft()
            for dr, dc in moves:
                rr = r + dr
                cc = c + dc
                if rr < 0  or rr >= h or cc < 0 or cc >= w:
                    continue
                if mat[rr][cc] != -1:
                    continue
                mat[rr][cc] = mat[r][c] + 1
                queue.append((rr, cc))
        return mat

mat = [[0,0,0],[0,1,0],[1,1,1]]
ans = Solution().updateMatrix(mat)
# assert ans == [[0,0,0],[0,1,0],[1,2,1]], ans

