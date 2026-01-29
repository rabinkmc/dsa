#include <stdbool.h>
#include <stdio.h>

int peak_idx(int *arr, int arrSize) {
    int idx = 0;
    for (int i = 0; i < arrSize; i++) {
        if (arr[i] > arr[idx]) {
            idx = i;
        };
    }
    return idx;
}

bool check_left(int *arr, int idx) {
    for (int i = idx; i > 0; i--) {
        if (arr[i] <= arr[i - 1]) {
            return false;
        }
    }
    return true;
}

bool check_right(int *arr, int idx, int arrSize) {
    for (int i = idx; i < arrSize - 1; i++) {
        if (arr[i] <= arr[i + 1]) {
            return false;
        }
    }
    return true;
}

bool validMountainArray(int *arr, int arrSize) {
    int idx = peak_idx(arr, arrSize);
    if (idx == 0 || idx == arrSize - 1) {
        return false;
    }
    bool left = check_left(arr, idx);
    bool right = check_right(arr, idx, arrSize);
    return left && right;
}

int main() {
    int arr[] = {1, 2, 3, 4, 3, 2, 1};
    int ans = validMountainArray(arr, 7);
    printf("array: %d", ans);
    return 0;
}
