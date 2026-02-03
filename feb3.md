## reviewing list operation in c

- insert 

a->b->d

1. insert in the middle
insert c after b means:
c points to where b pointed and b now points to c

2. insert at the end
last node points to the new node
a->b->d->e

3. insert at the front
new node points to the head of the list
new-node->next = head

- delete

1. delete at the middle
a->b->c->d (say let's delete c)
if we are to delete c, we have to first find the the node previous to c
and that prev->next = c->next
and then free(c)

how do we have the node previous to c
may be have two variables prev and curr
and when curr = c , return prev
I think that works.
prev = NULL
curr = head
while curr != NULL {
    if curr = c {
        return prev;
    }
    prev = curr;
    curr = curr->next;
}
node doesn't exist
err

2. delete at the end
easiest case, find the prev and prev->next = to-delete-node->next
and free the node

3. delete at the front
find the prev node and prev->next = to-delete-node->next
(this doesn't work because there is no prev node)
so if prev node is NULL, we have to delete the head node
a->b->c->d
lnode *a = head
head->next = head->next->next
delete(a)

### exercise 

1. lets create a node from 1 to 10
    a. delete some nodes
    b. insert missing nodes
    c. rearrange nodes like even and odd

- approach 1

prev = dummy
curr = head ( head is 1 in our case)

(-1 dummy) -> 1->2->3->4

we enter a loop from 2 to 10
prev->next = curr 
prev = curr
curr = new_node(i)

prev = head (at the start)
new_node = new_node(2) ( start from 2 )
prev->next = new_node;
prev = 


- approach 2: (is actually easier)
curr = 2

curr = 10

newnode is now 9
newnode->next curr
curr = newnode


I now understand tail and head much better, also the usage of dummy is clicking.
I would probably have to go over this again. 

Now, I have built the list. 

What can I do with it. Lets pick from a random number from 1 to max_node and
delete that number.

So, first, I need to understand the rand function in c.

So, there are two cases , one you have to be careful deleting at the front because
why change the head. 

if prev == NULL, that means we are at the head
so list = list->next, and free(curr)


To remove this special case, we can just add a dummy node at the front of the
list, and there will always be a prev and we can always assign to prev->next


2. lets insert a node in the list

1->2->4

insert 3 between 2 and 4, so we say insert at 2, rather than thinking in terms
of values


i.e insert(list, 2)
