#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
int cmp(const void *a, const void *b) {
    int x = *(const int *)a;
    int y = *(const int *)b;
    return (x > y) - (x < y);
}

bool search(int *arr, int left, int right, int target) {
    int mid;
    while (left <= right) {
        mid = left + (right - left) / 2;
        if (arr[mid] == target) {
            return true;
        } else if (arr[mid] > target) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    return false;
}

bool checkIfExist(int *arr, int arrSize) {
    qsort(arr, arrSize, sizeof(int), cmp);

    for (int i = 0; i < arrSize - 1; i++) {
        if (arr[i] == 0) {
            if (i + 1 < arrSize && arr[i + 1] == 0) {
                return true;
            }
            continue;
        }
        if (search(arr, 0, arrSize - 1, arr[i] * 2)) {
            return true;
        };
    }
    return false;
}

int main() {
    /*int arr[] = {10, 2, 5, 3};*/
    int arr[] = {0, -2, 2};
    /*int arr[] = {7, 1, 14, 11};*/
    /*int arr[] = {-10, 12, -20, -8, 15};*/
    printf("found: %d", checkIfExist(arr, 3));
    return 0;
}
