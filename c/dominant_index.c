#include <stdio.h>
int dominantIndex(int *nums, int numsSize) {
    int max_idx = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] > nums[max_idx]) {
            max_idx = i;
        }
    }
    for (int i = 0; i < numsSize; i++) {
        if (i == max_idx) {
            continue;
        }
        if (nums[i] * 2 > nums[max_idx]) {
            return -1;
        }
    }
    return max_idx;
}

int main() {
    int nums[] = {1, 2, 3, 4};
    printf("ans: %d", dominantIndex(nums, sizeof(nums) / sizeof(int)));
    return 0;
}
