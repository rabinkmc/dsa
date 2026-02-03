#include <stdio.h>
#include <stdlib.h>

#define X 1
#define O 2

typedef struct {
        int n;
        int *board;
} TicTacToe;

TicTacToe *ticTacToeCreate(int n) {
    TicTacToe *obj = (TicTacToe *)(malloc(sizeof(TicTacToe)));
    obj->board = calloc(n * n, sizeof(int));
    obj->n = n;
    return obj;
}

void render(TicTacToe *obj) {
    for (int i = 0; i < obj->n; i++) {
        printf("|");
        for (int j = 0; j < obj->n; j++) {
            int score = *((obj->board + i * obj->n + j));
            const char *mark = " X0";
            printf("%c|", mark[score]);
        }
        printf("\n");
    }
}
int score(TicTacToe *obj, int i, int j) {
    int rv = *((obj->board + i * obj->n + j));
    return rv;
}

int check(TicTacToe *obj, int player) {
    // check rows
    for (int i = 0; i < obj->n; i++) {
        int count = 0;
        for (int j = 0; j < obj->n; j++) {
            if (score(obj, i, j) == player) {
                count++;
            } else {
                break;
            }
        }
        if (count == obj->n) {
            return player;
        }
    }

    // check cols
    for (int j = 0; j < obj->n; j++) {
        int count = 0;
        for (int i = 0; i < obj->n; i++) {
            if (score(obj, i, j) == player) {
                count++;
            } else {
                break;
            }
        }
        if (count == obj->n) {
            return player;
        }
    }
    int count = 0;
    for (int i = 0; i < obj->n; i++) {
        if (score(obj, i, i) == player) {
            count++;
        }
    }
    if (count == obj->n) {
        return player;
    }

    count = 0;
    int r = obj->n - 1;
    int c = 0;
    for (int i = 0; i < obj->n; i++) {
        if (score(obj, r, c) == player) {
            count++;
        }
        r--;
        c++;
    }
    if (count == obj->n) {
        return player;
    }
    return 0;
}

int ticTacToeMove(TicTacToe *obj, int row, int col, int player) {
    *((obj->board + row * obj->n + col)) = player;
    return check(obj, player);
}

void ticTacToeFree(TicTacToe *obj) {
    free(obj->board);
    free(obj);
}

void clear_screen(void) {
    printf("\033[2J\033[H");
    fflush(stdout);
}
/**
 * Your TicTacToe struct will be instantiated and called as such:
 * TicTacToe* obj = ticTacToeCreate(n);
 * int param_1 = ticTacToeMove(obj, row, col, player);

 * ticTacToeFree(obj);
*/
int main(int argc, const char **argv) {
    if (argc < 2) {
        fprintf(stderr, "parameter n required\n");
        exit(EXIT_FAILURE);
    }
    int n = atoi(argv[1]);
    TicTacToe *obj = ticTacToeCreate(n);
    render(obj);
    int player = X;
    int moves = 0;
    while (moves < n * n) {
        clear_screen();
        render(obj);
        printf("\n Player %d turn\n", player);
        printf("Enter move (r, c): ");
        int r, c;
        scanf("%d, %d", &r, &c);
        if (ticTacToeMove(obj, r, c, player) == player) {
            clear_screen();
            render(obj);
            printf("player %d won\n", player);
            break;
        };
        player = 3 - player;
        moves++;
    }
    printf("Game ended in a tie\n");
    clear_screen();
    render(obj);
    return 0;
}
