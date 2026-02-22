#include <limits.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int r;
    int c;
} Point;

typedef struct {
    Point *buf;
    size_t head;
    size_t tail;
    size_t size;
    size_t cap;
} Queue;

Queue *queue_new(int cap) {
    Queue *q = malloc(sizeof(Queue));
    if (!q)
        return NULL;

    q->buf = malloc(cap * sizeof(Point));
    if (!q->buf) {
        free(q);
        return NULL;
    }
    q->head = 0;
    q->tail = 0;
    q->size = 0;
    q->cap = cap;
    return q;
}

static void queue_resize(Queue *q) {
    size_t new_cap = q->cap * 2;
    Point *new_buf = malloc(sizeof(Point) * new_cap);
    for (size_t i = 0; i < q->size; i++) {
        new_buf[i] = q->buf[(q->head + i) % q->cap];
    }
    free(q->buf);
    q->buf = new_buf;
    q->cap = new_cap;
    q->head = 0;
    q->tail = q->size;
}

void queue_push(Queue *q, Point p) {
    if (q->size == q->cap) {
        queue_resize(q);
    }
    q->buf[q->tail] = p;
    q->tail = (q->tail + 1) % q->cap;
    q->size++;
}

bool queue_pop(Queue *q, Point *out) {
    if (q->size == 0)
        return false;
    *out = q->buf[q->head];
    q->head = (q->head + 1) % q->cap;
    q->size--;
    return true;
}

bool queue_empty(Queue *q) { return q->size == 0; }

void queue_free(Queue *q) {
    free(q->buf);
    free(q);
}

void wallsAndGates(int **rooms, int roomSize, int *roomsColSize) {
    int rows = roomSize;
    int cols = roomsColSize[0];
    Queue *q = queue_new(16);
    if (!q)
        return;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (rooms[i][j] == 0) {
                queue_push(q, (Point){i, j});
            }
        }
    }
    int dirs[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    while (!queue_empty(q)) {
        Point curr;
        queue_pop(q, &curr);
        for (int d = 0; d < 4; d++) {
            int nr = curr.r + dirs[d][0];
            int nc = curr.c + dirs[d][1];
            if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) {
                continue;
            }
            if (rooms[nr][nc] != INT_MAX) {
                continue;
            }
            rooms[nr][nc] = rooms[curr.r][curr.c] + 1;
            queue_push(q, (Point){nr, nc});
        }
    }
    queue_free(q);
}

int main() {
    int rooms[4][4] = {{INT_MAX, -1, 0, INT_MAX},
        {INT_MAX, INT_MAX, INT_MAX, -1},
        {INT_MAX, -1, INT_MAX, -1},
        {0, -1, INT_MAX, INT_MAX}};

    printf("before\n");
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            if (rooms[i][j] == INT_MAX)
                printf("INF ");
            else
                printf("%d ", rooms[i][j]);
        }
        printf("\n");
    }

    int *room_ptrs[4];
    for (int i = 0; i < 4; i++) {
        room_ptrs[i] = rooms[i];
    }

    int cols = 4;
    wallsAndGates(room_ptrs, 4, &cols);

    printf("after\n");
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            if (rooms[i][j] == INT_MAX)
                printf("INF ");
            else
                printf("%d ", rooms[i][j]);
        }
        printf("\n");
    }

    return 0;
}
