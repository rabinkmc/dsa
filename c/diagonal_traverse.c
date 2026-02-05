#include <stdlib.h>

int *findDiagonalOrder(int **mat, int matSize, int *matColSize,
                       int *returnSize) {
    int i = 0;
    int j = 0;
    int m = matSize;
    int n = *matColSize;
    int *ans = (int *)calloc(m * n, sizeof(int));
    int k = 0;
    int dir = 1;
    while (k < m * n) {
        ans[k++] = mat[i][j];
        int r = dir ? i - 1 : i + 1;
        int c = dir ? j + 1 : j - 1;
        if (r < 0 || r == m || c < 0 || c == n) {
            if (dir) {
                if (j == n - 1) {
                    i++;
                } else {
                    j++;
                }
            } else {
                if (i == m - 1) {
                    j++;
                } else {
                    i++;
                }
            }
            dir = 1 - dir;
        } else {
            i = r;
            j = c;
        }
    }
    *returnSize = k;
    return ans;
}
