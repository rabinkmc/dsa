#ifndef HASHMAP_H
#define HASHMAP_H

#include <stdbool.h>

#define BUCKET_SIZE 1024

// Entry struct exposed so users can access key/value in iteration
typedef struct Entry {
        int key;
        int value;
        struct Entry *next;
} Entry;

// HashMap type
typedef struct HashMap HashMap;

// Iterator type
typedef struct HashIter HashIter;

// HashMap functions
HashMap *new_hashmap();
void hashmap_put(HashMap *map, int key, int value);
bool hashmap_get(HashMap *map, int key, int *value);
void hashmap_del(HashMap *map, int key);
void hashmap_free(HashMap *map);

// Iterator functions
HashIter *new_hashiter(HashMap *map);
Entry *hashiter_next(HashIter *it);

#endif
