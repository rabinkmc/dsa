#include <stdio.h>
int removeDuplicates(int *nums, int numsSize) {
    int idx = 0;
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] != nums[idx]) {
            idx++;
            nums[idx] = nums[i];
        }
    }
    return idx + 1;
}

int main() {
    int nums[] = {0, 0, 1, 1, 1, 2, 2, 3, 3, 4};
    int size = sizeof(nums) / sizeof(int);
    int count = removeDuplicates(nums, size);
    for (int i = 0; i < count; i++) {
        printf("%d ", nums[i]);
    }

    return 0;
}
