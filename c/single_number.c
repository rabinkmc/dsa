#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdint.h>

#define BUCKET_SIZE 1024

typedef struct Entry {
        int key;
        int value;
        struct Entry *next;
} Entry;

typedef struct {
        Entry **buckets;
} HashMap;

typedef struct {
        HashMap *map;
        Entry *curr;
        int bucket;
} HashIter;

uint32_t hash_int(int key) {
    uint32_t x = (uint32_t)key;
    x ^= x >> 16;
    x *= 0x7feb352d;
    x ^= x >> 15;
    x *= 0x846ca68b;
    x ^= x >> 16;

    return x;
}

int hash(int key) {
    return hash_int(key) % BUCKET_SIZE;
}

Entry *new_entry(int key, int value) {
    Entry *entry = malloc(sizeof(Entry));
    entry->key = key;
    entry->value = value;
    entry->next = NULL;
    return entry;
}

HashMap *new_hashmap() {
    HashMap *obj = malloc(sizeof(HashMap));
    obj->buckets = calloc(BUCKET_SIZE, sizeof(Entry *));
    return obj;
}

HashIter *new_hashiter(HashMap *map) {
    HashIter *it = malloc(sizeof(HashIter));
    it->map = map;
    it->bucket = -1;
    it->curr = NULL;
    return it;
}

void hashmapPut(HashMap *obj, int key, int value) {
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

void hashmapRemove(HashMap *obj, int key) {
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

int hashmapGet(HashMap *obj, int key) {
    int idx = hash(key);
    Entry *node = obj->buckets[idx];
    while (node) {
        if (node->key == key) {
            return node->value;
        }
        node = node->next;
    }
    return -1;
}

void free_bucket(Entry *entry) {
    while (entry) {
        Entry *tmp = entry;
        entry = entry->next;
        free(tmp);
    }
}

void hashmapFree(HashMap *obj) {
    for (int i = 0; i < BUCKET_SIZE; i++) {
        free_bucket(obj->buckets[i]);
    }
    free(obj->buckets);
    free(obj);
}

Entry *hash_iter_next(HashIter *it) {
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

int singleNumber(int *nums, int numsSize) {
    HashMap *counter = new_hashmap();
    for (int i = 0; i < numsSize; i++) {
        int value = hashmapGet(counter, nums[i]);
        if (value == -1) {
            hashmapPut(counter, nums[i], 1);
        } else {
            hashmapPut(counter, nums[i], value + 1);
        }
    }
    HashIter *it = new_hashiter(counter);
    Entry *e;
    while ((e = hash_iter_next(it))) {
        if (e->value == 1) {
            return e->key;
        }
    }
    return -1;
}

int main() {
    int nums[] = {2, 2, 1};
    int num = singleNumber(nums, sizeof(nums) / sizeof(int));
    printf("single number: %d\n", num);
    return 0;
}
