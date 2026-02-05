#include <stdio.h>

int findMaxConsecutiveOnes(int *nums, int numsSize) {
    int i = 0;
    int count = 0;
    int ans = 1;
    for (int j = 0; j < numsSize; j++) {
        if (nums[j] == 0) {
            count++;
        }
        while (count > 1) {
            if (nums[i] == 0) {
                count--;
            }
            i++;
        }
        if (j - i + 1 > ans) {
            ans = j - i + 1;
        };
    }
    return ans;
}

int main() {
    int nums[] = {1, 0, 1, 1, 0, 1, 1};
    int ans = findMaxConsecutiveOnes(nums, 7);
    printf("ans: %d", ans);
    return 0;
}
