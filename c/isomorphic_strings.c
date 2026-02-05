#include "hashmap.h"

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
    Entry *e;
    while ((e = hashiter_next(s_iter))) {
        printf("key %d, value %d\n", e->key, e->value);
    }
    printf("t counter\n");
    HashIter *t_iter = new_hashiter(t_counter);
    while ((e = hashiter_next(t_iter))) {
        printf("key %d, value %d\n", e->key, e->value);
    }
    return false;
}

int main() {
    bool status = isIsomorphic("egg", "add");
    printf("isomorphic: %d", status);
    return 0;
}
