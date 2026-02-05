from typing import List

class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        """
        I have to look on the diagonals, vertical and horizontal side
        """
        diag1 = []
        for i in range(8):
            diag1.append([i + j for j in range(8)])
        diag2 = diag1[::-1]

        kx, ky = king

        def same_diag(x1, y1, x2, y2):
            return diag1[x1][y1] == diag1[x2][y2] or diag2[x1][y1] == diag2[x2][y2]
        
        def same_line(x1, y1, x2, y2):
            return x1 == x2 or y1 == y2

        def check(qx, qy):
            if same_diag(qx, qy, kx, ky):
                # now check all the diagonals connecting queen and king
                xx = 1 if qx < kx else -1
                yy = 1 if qy < ky else -1  
                step = abs(qx - kx)
                for i in range(1, step):
                    px = qx +  i * xx
                    py = qy + i * yy
                    if [px, py] in queens:
                        break
                else:
                    return True

            elif qx == kx:
                yy = 1 if qy < ky else -1  
                step = abs(qy - ky)
                for i in range(1, step):
                    py = qy + i * yy
                    if [qx, py] in queens:
                        break
                else:
                    return True

            elif qy == ky:
                xx = 1 if qx < kx else -1
                step = abs(qx - kx)
                for i in range(1, step):
                    px = qx + i * xx
                    if [px, qy] in queens:
                        break
                else:
                    return True

            return False

        output = []
        for qx, qy in queens:
            if check(qx, qy):
                output.append([qx, qy])
        return output

Solution().queensAttacktheKing(queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0])
        
