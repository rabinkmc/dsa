#include <stdlib.h>

void merge(int *nums1, int nums1Size, int m, int *nums2, int nums2Size, int n) {
  int *arr = (int *)malloc(sizeof(int) * m);
  for (int i = 0; i < m; i++) {
    arr[i] = nums1[i];
  }
  int i, j, k;
  i = j = k = 0;
  while (i < m && j < n) {
    if (arr[i] < nums2[j]) {
      nums1[k] = arr[i];
      k++;
      i++;
    } else {
      nums1[k] = nums2[j];
      k++;
      j++;
    }
  }
  while (i < m) {
    nums1[k] = arr[i];
    k++;
    i++;
  }
  while (j < n) {
    nums1[k] = nums2[j];
    k++;
    j++;
  }
}

int main() {
  int nums1[6] = {4, 0, 0, 0, 0, 0};
  int nums2[5] = {1, 2, 3, 5, 6};
  merge(nums1, 6, 1, nums2, 5, 5);
}
