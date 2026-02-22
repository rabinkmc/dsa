#include <stdbool.h>
#include <stdlib.h>

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
    // very simple idea
    // if queue is full
    // double the capacity
    // copy all the old elements into new buffer
    // now data points to this new buffer
    // we can free old data
    // then it is just bookkeeping and updating the state
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

bool queue_deque(Queue *q) {
    if (queue_empty(q)) {
        return false;
    }
    q->head = (q->head + 1) % q->capacity;
    q->size--;
    return true;
}
int queue_rear(Queue *q) {
    if (queue_empty(q))
        return -1;
    size_t idx = (q->tail + q->capacity - 1) % q->capacity;
    return q->data[idx];
}

int queue_front(Queue *q) {
    if (queue_empty(q))
        return -1;
    return q->data[q->head];
}

/*int main() {*/
/*    size_t capacity = 5;*/
/*    Queue *q = queue_new(capacity);*/
/*    queue_enqueue(q, 1);*/
/*    queue_enqueue(q, 2);*/
/*    queue_enqueue(q, 3);*/
/*    queue_deque(q);*/
/*    queue_deque(q);*/
/*    queue_enqueue(q, 4);*/
/*    queue_enqueue(q, 5);*/
/*    queue_enqueue(q, 6);*/
/*    queue_enqueue(q, 7);*/
/*    queue_enqueue(q, 8);*/
/*    return 0;*/
/*}*/
