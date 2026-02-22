CC      = gcc
CFLAGS  = -Wall -Wextra -std=c23 -Iinclude

# Problem file (default)
SRC ?= src.c
MAIN_OBJ = $(SRC:.c=.o)

# Library (fixed)
LIB_SRC = hashmap.c array.c
LIB_OBJ = $(LIB_SRC:.c=.o)

TARGET  = app

.PHONY: all run clean

all: $(TARGET)

$(TARGET): $(MAIN_OBJ) $(LIB_OBJ)
	$(CC) $(CFLAGS) $^ -o $(TARGET)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

run: $(TARGET)
	./$(TARGET)

clean:
	rm -f *.o $(TARGET)
