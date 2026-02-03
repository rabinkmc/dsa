#include <stdio.h>

void duplicateZeros(int *arr, int arrSize) {
  int possible_dups = 0;
  int length = arrSize - 1;
  for (int left = 0; left <= length; left++) {
    if (left > length - possible_dups) {
      break;
    }
    if (arr[left] == 0) {
      if (left == length - possible_dups) {
        arr[length] = 0;
        length--;
        break;
      }
      possible_dups++;
    }
  }
  int last = length - possible_dups;
  for (int i = last; i >= 0; i--) {
    if (arr[i] == 0) {
      arr[i + possible_dups] = 0;
      possible_dups--;
      arr[i + possible_dups] = 0;
    } else {
      arr[i + possible_dups] = arr[i];
    }
  }
}

int main() {
  int arr[] = {1, 0, 2, 3, 0, 4, 5, 0};
  int arrSize = sizeof(arr) / sizeof(int);
  duplicateZeros(arr, arrSize);
  for (int i = 0; i < arrSize; i++) {
    printf("%d  ", arr[i]);
  }
  return 0;
}
