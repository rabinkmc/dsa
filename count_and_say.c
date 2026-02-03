#include <stdlib.h>
#include <string.h>
#include <stdio.h>

char *f(const char *s) {
    int len = strlen(s);
    char *arr = malloc(len * 2 + 1);
    int j = 0;
    int count = 1;
    int i = 1;
    for (i = 1; s[i]; i++) {
        if (s[i] == s[i - 1]) {
            count++;
        } else {
            j += sprintf(arr + j, "%d%c", count, s[i - 1]);
            count = 1;
        }
    }
    j += sprintf(arr + j, "%d%c", count, s[i - 1]);
    arr[j] = '\0';
    return arr;
}

char *countAndSay(int n) {
    char *res = malloc(2);
    strcpy(res, "1");
    for (int i = 2; i <= n; i++) {
        char *next = f(res);
        free(res);
        res = next;
    }
    return res;
}
