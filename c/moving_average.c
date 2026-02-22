#include <stdlib.h>
#include <stdio.h>

typedef struct {
        double *data;
        int size;
        int capacity;
        int idx;
        double sum;
} MovingAverage;

MovingAverage *movingAverageCreate(int size) {
    if (size <= 0) {
        return NULL;
    }
    MovingAverage *obj = malloc(sizeof(MovingAverage));
    obj->data = calloc(size, sizeof(double));
    obj->capacity = size;
    obj->size = 0;
    obj->idx = -1;
    obj->sum = 0.0;
    return obj;
}

double sum(MovingAverage *obj) {
    double total = 0;
    for (int i = 0; i < obj->size; i++) {
        total += obj->data[i];
    }
    return total;
};

double movingAverageNext(MovingAverage *obj, int val) {
    obj->idx = (obj->idx + 1) % obj->capacity;
    if (obj->size == obj->capacity) {
        // remove the last element
        obj->sum = obj->sum - obj->data[obj->idx];
    } else {
        obj->size++;
    }
    obj->data[obj->idx] = val;
    obj->sum += val;
    return obj->sum / obj->size;
}

void movingAverageFree(MovingAverage *obj) {
    free(obj->data);
    free(obj);
}

int main() {
    int size = 3;
    MovingAverage *obj = movingAverageCreate(size);
    if (!obj) {
        fprintf(stderr, "cannot create window of size 0\n");
        exit(1);
    }
    movingAverageNext(obj, 100);
    movingAverageNext(obj, 100);
    movingAverageNext(obj, 3);
    double avg = movingAverageNext(obj, 5);
    printf("average %.2f", avg);

    movingAverageFree(obj);
    return 0;
}
