#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

int str_to_int(char *s) {
    int res = 0;
    for (int i = 0; i < 4; i++) {
        res = res * 10 + (s[i] - '0');
    }
    return res;
}

typedef struct Queue {
    int *data;
    size_t size;
    size_t capacity;
    size_t head;
    size_t tail;
} Queue;

Queue *queue_new(int capacity) {
    if (capacity == 0) {
        return NULL;
    }
    Queue *q = malloc(sizeof(Queue));
    if (!q)
        return NULL;
    q->data = calloc(capacity, sizeof(int));
    if (!q->data) {
        free(q);
        return NULL;
    }
    q->size = 0;
    q->head = 0;
    q->tail = 0;
    q->capacity = capacity;

    return q;
}

bool queue_empty(Queue *q) { return q->size == 0; }

bool queue_full(Queue *q) { return q->size == q->capacity; }

bool queue_enqueue(Queue *q, int value) {
    if (queue_full(q)) {
        size_t new_cap = q->capacity * 2;
        int *new_buf = calloc(new_cap, sizeof(int));
        if (!new_buf)
            return false;
        for (size_t i = 0; i < q->size; i++) {
            new_buf[i] = q->data[(q->head + i) % q->capacity];
        }
        free(q->data);
        q->data = new_buf;
        q->capacity = new_cap;
        q->head = 0;
        q->tail = q->size;
    }
    q->data[q->tail] = value;
    q->tail = (q->tail + 1) % q->capacity;
    q->size++;
    return true;
}

bool queue_deque(Queue *q, int *out) {
    if (queue_empty(q)) {
        return false;
    }
    *out = q->data[q->head];
    q->head = (q->head + 1) % q->capacity;
    q->size--;
    return true;
}

void queue_free(Queue *q) {
    free(q->data);
    free(q);
}

int openLock(char **deadends, int deadendsSize, char *target) {
    Queue *q = queue_new(100);
    bool visited[10000] = {false};
    bool dead[10000] = {false};
    int dest = str_to_int(target);
    for (int i = 0; i < deadendsSize; i++) {
        size_t pos = str_to_int(deadends[i]);
        dead[pos] = true;
    }
    int start = 0;
    if (dead[start]) {
        return -1;
    }
    if (dest == start) {
        return 0;
    }
    queue_enqueue(q, 0);
    int steps = 0;
    while (!queue_empty(q)) {
        steps++;
        size_t sz = q->size;
        // 1234
        int powers[4] = {1, 10, 100, 1000};
        for (size_t i = 0; i < sz; i++) {
            int curr;
            queue_deque(q, &curr);
            for (size_t pos = 0; pos < 4; pos++) {
                int pow10 = powers[pos];
                int digit = (curr / pow10) % 10;
                for (int delta = -1; delta <= 1; delta = delta + 2) {
                    int nextDigit = (digit + delta + 10) % 10;
                    int next = curr - pow10 * digit + nextDigit * pow10;
                    if (next == dest) {
                        queue_free(q);
                        return steps;
                    }
                    if (visited[next] || dead[next]) {
                        continue;
                    }
                    visited[next] = true;
                    queue_enqueue(q, next);
                }
            }
        }
    }
    queue_free(q);
    return -1;
}

int main() {
    char *deadends[] = {
        "0201",
        "0101",
        "0102",
        "1212",
        "2002",
    };
    int deadendsSize = 5;
    char *target = "0009";
    int res = openLock(deadends, deadendsSize, target);
    printf("answer : %d", res);
}
