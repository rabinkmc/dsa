#ifndef ARRAY_H
#define ARRAY_H

#include <stddef.h>

typedef struct {
        int *data;
        size_t size;
        size_t capacity;
} Array;

Array *array_new(void);
void array_append(Array *arr, int value);
int array_pop(Array *arr);
int array_len(Array *arr);
void array_free(Array *arr);
void array_sort(Array *arr);

void array_print(Array *arr);

#endif
