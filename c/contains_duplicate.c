#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdint.h>

#define BUCKET_SIZE 1024
typedef struct Entry {
        int key;
        struct Entry *next;
} Entry;
typedef struct {
        Entry **buckets;
} HashSet;

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

Entry *new_entry(int key) {
    Entry *entry = malloc(sizeof(Entry));
    entry->key = key;
    entry->next = NULL;
    return entry;
}

HashSet *new_hashset() {
    HashSet *obj = malloc(sizeof(HashSet));
    obj->buckets = calloc(BUCKET_SIZE, sizeof(Entry *));
    return obj;
}

void hashsetAdd(HashSet *obj, int key) {
    int idx = hash(key);
    Entry *node = obj->buckets[idx];
    while (node) {
        if (node->key == key) return;
        node = node->next;
    }
    Entry *entry = new_entry(key);
    entry->next = obj->buckets[idx];
    obj->buckets[idx] = entry;
}

void hashsetRemove(HashSet *obj, int key) {
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

bool hashsetContains(HashSet *obj, int key) {
    int idx = hash(key);
    Entry *node = obj->buckets[idx];
    while (node) {
        if (node->key == key) {
            return true;
        }
        node = node->next;
    }
    return false;
}

void free_bucket(Entry *entry) {
    while (entry) {
        Entry *tmp = entry;
        entry = entry->next;
        free(tmp);
    }
}

void hashsetFree(HashSet *obj) {
    for (int i = 0; i < BUCKET_SIZE; i++) {
        free_bucket(obj->buckets[i]);
    }
    free(obj->buckets);
    free(obj);
}

bool containsDuplicate(int *nums, int numsSize) {
    HashSet *set = new_hashset();
    for (int i = 0; i < numsSize; i++) {
        if (hashsetContains(set, nums[i])) {
            hashsetFree(set);
            return true;
        }
        hashsetAdd(set, nums[i]);
    }
    hashsetFree(set);
    return false;
}

int main() {
    int arr[4] = {1, 2, 3, 1};
    printf("status: %d\n", containsDuplicate(arr, sizeof(arr) / sizeof(int)));
    return 0;
}
