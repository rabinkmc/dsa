#include <stdlib.h>
#include <string.h>
#include <stdio.h>

int all_nines(int *digits, int digitSize) {
    for (int i = 0; i < digitSize; i++) {
        if (digits[i] != 9) {
            return 0;
        }
    }
    return 1;
}

int *plusOne(int *digits, int digitsSize, int *returnSize) {
    if (all_nines(digits, digitsSize)) {
        int *ans = (int *)calloc(digitsSize + 1, sizeof(int));
        *returnSize = digitsSize + 1;
        ans[0] = 1;
        return ans;
    }
    int size = sizeof(int) * digitsSize;
    int *ans = (int *)malloc(size);
    memcpy(ans, digits, size);
    *returnSize = digitsSize;

    int j = digitsSize - 1;
    while (digits[j] == 9) {
        ans[j] = 0;
        j--;
    }
    ans[j] += 1;
    return ans;
}

int main() {
    int rs = 0;
    int digits[] = {1, 0, 0, 0};
    int *ans = plusOne(digits, sizeof(digits) / sizeof(int), &rs);
    printf("rs: %d\n", rs);
    for (int i = 0; i < rs; i++) {
        printf("%d ", ans[i]);
    }
    return 0;
}
