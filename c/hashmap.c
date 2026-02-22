#include "include/hashmap.h"
#include <stdlib.h>
#include <stdint.h>
#include <stdio.h>

// Full struct definitions
struct HashMap {
        Entry **buckets;
};

struct HashIter {
        HashMap *map;
        Entry *curr;
        int bucket;
};

// Hash function
static uint32_t hash_int(int key) {
    uint32_t x = (uint32_t)key;
    x ^= x >> 16;
    x *= 0x7feb352d;
    x ^= x >> 15;
    x *= 0x846ca68b;
    x ^= x >> 16;
    return x;
}

static int hash(int key) {
    return hash_int(key) % BUCKET_SIZE;
}

// Entry creation
static Entry *new_entry(int key, int value) {
    Entry *entry = malloc(sizeof(Entry));
    entry->key = key;
    entry->value = value;
    entry->next = NULL;
    return entry;
}

// HashMap creation
HashMap *new_hashmap() {
    HashMap *obj = malloc(sizeof(HashMap));
    obj->buckets = calloc(BUCKET_SIZE, sizeof(Entry *));
    return obj;
}

// Iterator creation
HashIter *new_hashiter(HashMap *map) {
    HashIter *it = malloc(sizeof(HashIter));
    it->map = map;
    it->bucket = -1;
    it->curr = NULL;
    return it;
}

// Put key/value
void hashmap_put(HashMap *obj, int key, int value) {
    int idx = hash(key);
    Entry *node = obj->buckets[idx];
    while (node) {
        if (node->key == key) {
            node->value = value;
            return;
        }
        node = node->next;
    }
    Entry *entry = new_entry(key, value);
    entry->next = obj->buckets[idx];
    obj->buckets[idx] = entry;
}

// Delete key
void hashmap_del(HashMap *obj, int key) {
    int idx = hash(key);
    Entry *node = obj->buckets[idx];
    Entry dummy = {.next = node};
    Entry *prev = &dummy;
    while (node) {
        if (node->key == key) {
            prev->next = node->next;
            free(node);
            obj->buckets[idx] = dummy.next;
            return;
        }
        prev = node;
        node = node->next;
    }
}

// Get value
bool hashmap_get(HashMap *obj, int key, int *value) {
    int idx = hash(key);
    Entry *node = obj->buckets[idx];
    while (node) {
        if (node->key == key) {
            *value = node->value;
            return true;
        }
        node = node->next;
    }
    return false;
}

// Free bucket
static void free_bucket(Entry *entry) {
    while (entry) {
        Entry *tmp = entry;
        entry = entry->next;
        free(tmp);
    }
}

// Free HashMap
void hashmap_free(HashMap *obj) {
    for (int i = 0; i < BUCKET_SIZE; i++) {
        free_bucket(obj->buckets[i]);
    }
    free(obj->buckets);
    free(obj);
}

// Iterator next
Entry *hashiter_next(HashIter *it) {
    if (it->curr && it->curr->next) {
        it->curr = it->curr->next;
        return it->curr;
    }
    for (it->bucket += 1; it->bucket < BUCKET_SIZE; it->bucket++) {
        Entry *curr = it->map->buckets[it->bucket];
        if (curr) {
            it->curr = curr;
            return curr;
        }
    }
    return NULL;
}
