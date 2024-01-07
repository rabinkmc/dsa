class Solution:
    def minMovesToCaptureTheQueen(
        self, a: int, b: int, c: int, d: int, e: int, f: int
    ) -> int:
        if a == e or b == f:
            if not (a == c or b == d):
                return 1
            if not ((a > c > e) or (a < c < e) or (b > d > f) or (b < d < f)):
                return 1
            if abs(c - e) % 2 == 0 or abs(b - f) % 2 == 0:
                return 2
            return 3
        diag1 = [list(range(i, i + 8)) for i in range(1, 8 + 1)]
        diag2 = diag1[::-1]
        a, b, c, d, e, f = a - 1, b - 1, c - 1, d - 1, e - 1, f - 1
        rook_on_bishop_line = diag1[c][d] == diag1[a][b] or diag2[c][d] == diag2[a][b]
        if diag1[e][f] == diag1[c][d] or diag2[e][f] == diag2[c][d]:
            if not rook_on_bishop_line:
                return 1
            # queen > rook > bishop
            # bishop > rook > queen
            if (e > a > c) or (e < a < c) or (f > b > d) or (f < b < d):
                return 2
            return 1
        return 2

a, b, c, d, e, f = 7, 3, 4, 4, 5, 2
a, b, c, d, e, f = 4, 3, 3, 4, 5, 2
a, b, c, d, e, f = 1, 1, 1, 4, 1, 8
ans = Solution().minMovesToCaptureTheQueen(a, b, c, d, e, f)
print(ans)
