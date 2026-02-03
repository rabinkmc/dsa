#include <stdio.h>
#include <stdlib.h>

int cmp(const void *a, const void *b) {
    int x = *(const int *)a;
    int y = *(const int *)b;

    return (x > y) - (x < y);
}

int thirdMax(int *nums, int numsSize) {
    qsort(nums, numsSize, sizeof(int), cmp);
    if (numsSize <= 2) {
        return nums[numsSize - 1];
    }
    int k = 1;
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] != nums[k - 1]) {
            nums[k++] = nums[i];
        }
    }
    if (k < 3) {
        return nums[k - 1];
    }
    return nums[k - 3];
}

int main() {
    int nums[] = {2, 2, 3, 1};
    int size = sizeof(nums) / sizeof(int);
    int third_max = thirdMax(nums, size);
    printf("third_max : %d\n", third_max);
    return 0;
}
