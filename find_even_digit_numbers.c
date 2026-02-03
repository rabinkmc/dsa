#include <stdio.h>
int digit_size(int num) {
  int size = 0;
  while (num) {
    num = num / 10;
    size++;
  }
  return size;
}
int findNumbers(int *nums, int numsSize) {
  int ans = 0;
  for (int i = 0; i < numsSize; i++) {
    int size = digit_size(nums[i]);
    printf("digit_size(%d)==%d\n", nums[i], size);
    if (size % 2 == 0) {
      ans++;
    }
  }
  return ans;
}

int main() {
  int nums[5] = {12, 345, 2, 6, 7896};
  int ans = findNumbers(nums, 5);
  printf("%d", ans);
  return 0;
}
