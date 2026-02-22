#include "include/hashmap.h"
#include "include/array.h"

#include <stdio.h>

bool isIsomorphic(char *s, char *t) {
    HashMap *s_counter = new_hashmap();
    HashMap *t_counter = new_hashmap();
    for (; *s; s++) {
        int value;
        if (hashmap_get(s_counter, *s, &value)) {
            hashmap_put(s_counter, *s, value + 1);
        } else {
            hashmap_put(s_counter, *s, 1);
        };
    }
    for (; *t; t++) {
        int value;
        if (hashmap_get(s_counter, *t, &value)) {
            hashmap_put(s_counter, *t, value + 1);
        } else {
            hashmap_put(s_counter, *t, 1);
        };
    }
    HashIter *s_iter = new_hashiter(s_counter);
    HashIter *t_iter = new_hashiter(t_counter);
    Entry *e;
    Array *s_arr = array_new();
    Array *t_arr = array_new();
    while ((e = hashiter_next(s_iter))) {
        array_append(s_arr, e->value);
    }
    while ((e = hashiter_next(t_iter))) {
        array_append(t_arr, e->value);
    }
    if (array_len(s_arr) != array_len(t_arr)) {
        return false;
    }
    array_sort(s_arr);
    array_sort(t_arr);
    for (int i = 0; i < array_len(s_arr); i++) {
        if (s_arr->data[i] != t_arr->data[i]) {
            return false;
        }
    }
    return false;
}

int main() {
    int status = isIsomorphic("egg", "add");
    printf("isomorphic: %d", status);
    return 0;
}
