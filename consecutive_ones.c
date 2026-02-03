#include <stdio.h>

int max(int a, int b) {
  if (a > b) {
    return a;
  } else {
    return b;
  }
}

int findMaxConsecutiveOnes(int *nums, int numsSize) {
  int ans = 0;
  int curr = 0;
  for (int i = 0; i < numsSize; i++) {
    if (nums[i] == 0) {
      ans = max(ans, curr);
      curr = 0;
    } else {
      curr++;
    }
  }
  ans = max(ans, curr);
  return ans;
}

int main() {
  int nums[6] = {1, 1, 0, 1, 1, 1};
  int ans = findMaxConsecutiveOnes(nums, 6);
  printf("ans: %d\n", ans);
}
