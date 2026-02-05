#include <stdlib.h>
#include <stdio.h>

void print(int *arr, int size) {
    printf("{");
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("}\n");
}

int pivotIndex(int *nums, int numsSize) {
    int *prefix = (int *)calloc(numsSize + 1, sizeof(int));
    int *suffix = (int *)calloc(numsSize + 1, sizeof(int));
    for (int i = 0; i < numsSize; i++) {
        prefix[i + 1] = prefix[i] + nums[i];
    }
    /*printf("prefix: ");*/
    /*print(prefix, numsSize + 1);*/
    for (int i = numsSize - 1; i > -1; i--) {
        suffix[i] = suffix[i + 1] + nums[i];
    }
    /*printf("suffix: ");*/
    /*print(suffix, numsSize + 1);*/
    /*printf("nums:   ");*/
    /*print(nums, numsSize);*/

    for (int i = 0; i < numsSize; i++) {
        if (prefix[i] == suffix[i + 1]) {
            return i;
        }
    }

    free(prefix);
    free(suffix);
    return -1;
}

int main() {
    int nums[] = {1, 7, 3, 6, 5, 6};
    int ans = pivotIndex(nums, sizeof(nums) / sizeof(int));
    printf("index: %d", ans);
    return 0;
}
