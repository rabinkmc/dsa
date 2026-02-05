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
} MyHashSet;

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

MyHashSet *myHashSetCreate() {
    MyHashSet *obj = malloc(sizeof(MyHashSet));
    obj->buckets = calloc(BUCKET_SIZE, sizeof(Entry *));
    return obj;
}

void myHashSetAdd(MyHashSet *obj, int key) {
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

void myHashSetRemove(MyHashSet *obj, int key) {
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

bool myHashSetContains(MyHashSet *obj, int key) {
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

void myHashSetFree(MyHashSet *obj) {
    for (int i = 0; i < BUCKET_SIZE; i++) {
        free_bucket(obj->buckets[i]);
    }
    free(obj->buckets);
    free(obj);
}

int main() {
    MyHashSet *obj = myHashSetCreate();
    myHashSetAdd(obj, 1);

    myHashSetRemove(obj, 1);

    bool param_3 = myHashSetContains(obj, 1);
    printf("%d", param_3);

    myHashSetFree(obj);
    return 0;
}
