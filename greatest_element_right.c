#include <stdio.h>
int *replaceElements(int *arr, int arrSize, int *returnSize) {
    int maxr = -1;
    for (int i = arrSize - 1; i >= 0; i--) {
        int v = arr[i];
        arr[i] = maxr;
        if (v > maxr) {
            maxr = v;
        }
    }
    *returnSize = arrSize;
    return arr;
}

int main() {
    int arr[] = {17, 18, 5, 4, 6, 1};
    int rs = 0;
    int *ans = replaceElements(arr, 6, &rs);
    for (int i = 0; i < 6; i++) {
        printf("%d ", ans[i]);
    }
    return 0;
}
