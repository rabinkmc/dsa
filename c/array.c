#include "include/array.h"
#include <stdio.h>
#include <stdlib.h>

Array *array_new() {
    Array *arr = malloc(sizeof(Array));
    arr->size = 0;
    arr->capacity = 4;
    arr->data = calloc(arr->capacity, sizeof(int));
    return arr;
}

void array_append(Array *arr, int value) {
    if (arr->size == arr->capacity) {
        arr->capacity *= 2;
        arr->data = realloc(arr->data, arr->capacity * sizeof(int));
    }
    arr->data[arr->size++] = value;
}

int array_pop(Array *arr) {
    if (arr->size == 0) {
        fprintf(stderr, "Error: pop from empty array\n");
        exit(1);
    }
    arr->size--;
    return arr->data[arr->size];
}

void array_print(Array *arr) {
    printf("[");
    for (size_t i = 0; i < arr->size; i++) {
        if (i != arr->size - 1) printf(", ");
    }
    printf("]\n");
}

int cmp_int(const void *a, const void *b) {
    int x = *(const int *)a;
    int y = *(const int *)b;
    return (x > y) - (x < y); // returns 1, -1, or 0
}

void array_sort(Array *arr) {
    if (arr->size > 1) {
        qsort(arr->data, arr->size, sizeof(int), cmp_int);
    }
}

int array_len(Array *arr) {
    return arr->size;
}

void array_free(Array *arr) {
    free(arr->data);
    free(arr);
}
