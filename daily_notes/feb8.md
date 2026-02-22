## Problem 1: design circular queue

What I am thinking of is firstly just a singly linked list should work just
fine. You can keep track of head and tail pointers and just make sure the tail
pointer is always pointing to the head and we have a circular queue.
Everything else is just detail.


1. first method , simply use a linked list with head and tail pointer

2. Ring Buffer -> This is the approach I don't know about.

## Problem 2: moving average data stream

i think rolling index works here

## Problem 3: queue and BFS

undestanding why you should use ring buffer for queue

**Example 1**
capacity = 5
buf = [_, _, _, _, _]
head = 0
tail = 0

enqueue -> 1, 2, 3
buf = [1, 2, 3, _, _]
head = 0
tail = 3

deque -> head = 1
deque -> head = 2

enqueue 4, tail -> 4
enque 5, tail -> 5 , beyond array

Although there are just three elements and we have empty slots, we have run out
of space.

## Problem 4: Walls and gates

Now, lets take a step back and use bfs

I have a queue starting out with gates as starting nodes.

I think this problem was very helpful for me. Obviously, I have learnt to lot
still but there isn't that intimidation and fear of C. It's a perfect language
to write your code. It's just that you can build everything from it but it
doesn't give you any tools.
