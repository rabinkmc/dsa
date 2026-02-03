#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define TABLE_SIZE 1024

typedef struct Entry {
  char *key;
  int value;
  struct Entry *next;
} Entry;

typedef struct HashMap {
  Entry **buckets;
  size_t size;
} HashMap;

unsigned int hash(const char *key) {
  unsigned int h = 5381;
  while (*key) {
    h = ((h << 5) + h) + *key; // h * 33 + c
    key++;
  }
  return h % TABLE_SIZE;
}

void hashmap_put(HashMap *map, char *key, int value) {
  unsigned int idx = hash(key) % map->size;
  Entry *e = map->buckets[idx];
  while (e) {
    if (strcmp(e->key, key) == 0) {
      e->value = value;
      return;
    }
    e = e->next;
  }
  Entry *new = malloc(sizeof(Entry));
  new->key = strdup(key);
  new->value = value;
  new->next = map->buckets[idx];
  map->buckets[idx] = new;
}

int hashmap_get(HashMap *map, const char *key, int *found) {
  unsigned int idx = hash(key) % map->size;
  Entry *e = map->buckets[idx];
  while (e) {
    if (strcmp(e->key, key) == 0) {
      *found = 1;
      return e->value;
    }
  }
  *found = 0;
  return 0;
}

HashMap *map_create(size_t size) {
  HashMap *m = malloc(sizeof(HashMap));
  m->size = size;
  m->buckets = calloc(size, sizeof(Entry *));
  return m;
}

int main(int argc, const char **argv) {
  HashMap *map = map_create(1024);
  hashmap_put(map, "rabin", 1);
  hashmap_put(map, "angela", 2);
  int found = 0;
  printf("%d\n", hashmap_get(map, "rabin", &found));
  found = 0;
  printf("%d\n", hashmap_get(map, "angela", &found));
  return 0;
}
