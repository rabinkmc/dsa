#include <stdio.h>

int removeElement(int *nums, int numsSize, int val) {
  int count = 0;
  for (int i = 0; i < numsSize; i++) {
    if (nums[i] == val) {
      count++;
    }
  }
  int j = 0;
  for (int i = 0; i < numsSize; i++) {
    if (nums[i] == val) {
      continue;
    }
    nums[j] = nums[i];
    j++;
  }
  return numsSize - count;
}

int main() {
  int nums[8] = {0, 1, 2, 2, 3, 0, 4, 2};
  int count = removeElement(nums, 8, 2);
  for (int i = 0; i < 8 - count; i++) {
    printf("%d ", nums[i]);
  }
}
