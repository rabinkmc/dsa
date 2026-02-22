## problem 1: number of islands
## problem 2: open the lock
## problem 3: min stack
Approach 1:
use two values in the stack, one the x, another min so far including x

12, 30, 7, 6, 45, 2, 11, 27, 15

12-12, 30-12 

## problem 4: daily temperatures

## problem 5: implement queue using stack

two stacks
1. push stack
2. pop stack (if no element to pop in pop stacks pop all the elements from push
   stack)

## problem 6: matrix_01

idea is to do a single bfs. What I was doing was multiple bfs, i.e from each 1 i
was trying to find nearest 0

but this is slow compared to single bfs

you append all the 0's to the queue and whenever you encounter 1 , you simply
update the output grid with current step. 

## problem 7: keys and rooms

This is very simple, rooms is basically a graph, and we have to make sure all of
the cells are visited. For this you could check if visited is True for all rooms
or simply keep track of count
