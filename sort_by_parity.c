/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include <stdlib.h>
#include <stdio.h>

int *sortArrayByParity(int *nums, int numsSize, int *returnSize) {
    int *tmp = malloc(sizeof(int) * numsSize);
    int idx = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] % 2 == 0) {
            tmp[idx++] = nums[i];
        }
    }
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] % 2 == 1) {
            tmp[idx++] = nums[i];
        }
    }
    *returnSize = numsSize;
    return tmp;
}

int main() {
    int nums[] = {3, 1, 2, 4};
    int rs = 0;
    int *ans = sortArrayByParity(nums, 4, &rs);
    for (int i = 0; i < 4; i++) {
        printf("%d ", ans[i]);
    }
    return 0;
}
