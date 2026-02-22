#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int r;
    int c;
} Point;

typedef struct Stack {
    Point *data;
    size_t top;
    size_t capacity;
} stack_t;

stack_t *stack_new(int capacity) {
    if (capacity == 0) {
        return NULL;
    }
    stack_t *s = malloc(sizeof(stack_t));
    if (!s) {
        return NULL;
    }
    s->data = malloc(sizeof(Point) * capacity);
    if (!s->data) {
        free(s);
        return NULL;
    }
    s->top = 0;
    s->capacity = capacity;
    return s;
}

void stack_free(stack_t *s) {
    if (!s) {
        return;
    }
    free(s->data);
    free(s);
}

void stack_resize(stack_t *s) {
    size_t new_cap = s->capacity * 2;
    Point *new_data = realloc(s->data, sizeof(Point) * new_cap);
    if (!new_data) {
        return;
    }
    s->data = new_data;
    s->capacity = new_cap;
}

bool stack_empty(const stack_t *s) { return s->top == 0; }
bool stack_full(const stack_t *s) { return s->top == s->capacity; }

bool stack_push(stack_t *s, Point p) {
    if (s->top == s->capacity) {
        stack_resize(s);
    }
    s->data[s->top++] = p;
    return true;
}

bool stack_pop(stack_t *s, Point *out) {
    if (stack_empty(s)) {
        return false;
    }
    *out = s->data[--s->top];
    return true;
}

void dfs(char **grid, int rows, int cols, int r, int c) {
    stack_t *s = stack_new(rows * cols);
    grid[r][c] = '#';
    stack_push(s, (Point){r, c});

    int dirs[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    while (!stack_empty(s)) {
        Point curr;
        stack_pop(s, &curr);
        for (int d = 0; d < 4; d++) {
            int nr = curr.r + dirs[d][0];
            int nc = curr.c + dirs[d][1];
            if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) {
                continue;
            }
            if (grid[nr][nc] == '#') {
                continue;
            }
            if (grid[nr][nc] == '1') {
                grid[nr][nc] = '#';
                stack_push(s, (Point){nr, nc});
            }
        }
    }
    stack_free(s);
}

int numIslands(char **grid, int gridSize, int *gridColSize) {
    int count = 0;
    int rows = gridSize;
    int cols = gridColSize[0];
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (grid[i][j] == '1') {
                dfs(grid, rows, cols, i, j);
                count++;
            }
        }
    }
    return count;
}

int main() {
    char grids[4][5] = {
        {'1', '1', '0', '1', '0'},
        {'1', '1', '0', '1', '0'},
        {'1', '1', '0', '1', '0'},
        {'1', '1', '0', '1', '0'},
    };
    char *grid[4];
    for (int i = 0; i < 4; i++) {
        grid[i] = grids[i];
    }
    int cols = 5;
    int ans = numIslands(grid, 4, &cols);
    printf("answer: %d", ans);
    return 0;
}
