#include <stdio.h>
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int square(int x) { return x * x; }

int *sortedSquares(int *nums, int numsSize, int *returnSize) {
  int left = 0;
  int right = numsSize - 1;
  int *res = (int *)malloc(sizeof(int) * numsSize);
  for (int i = numsSize - 1; i > -1; i--) {
    int tmp = 0;
    if (square(nums[left]) < square(nums[right])) {
      tmp = square(nums[right]);
      right--;
    } else {
      tmp = square(nums[left]);
      left++;
    }
    res[i] = tmp;
  }
  *returnSize = numsSize;
  return res;
}

int main() {
  int nums[5] = {-4, -1, 0, 3, 10};
  int returnSize = 5;

  int *ans = sortedSquares(nums, 5, &returnSize);
  printf("{");
  for (int i = 0; i < returnSize; i++) {
    printf("%d  ", ans[i]);
  }
  printf("}\n");
  return 0;
}
