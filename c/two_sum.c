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

bool hashmapGet(HashMap *obj, int key, int *value) {
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
int *twoSum(int *nums, int numsSize, int target, int *returnSize) {
    int *ans = malloc(sizeof(int) * 2);
    *returnSize = 2;
    HashMap *seen = new_hashmap();
    for (int i = 0; i < numsSize; i++) {
        int idx;
        if (hashmapGet(seen, target - nums[i], &idx)) {
            ans[0] = idx;
            ans[1] = i;
            return ans;
        };
        hashmapPut(seen, nums[i], i);
    }
    return ans;
}

int main() {
    int nums[] = {0, 17, 7, 2};
    int rs;
    int *ans = twoSum(nums, 4, 9, &rs);
    printf("{%d, %d}", ans[0], ans[1]);
    return 0;
}
