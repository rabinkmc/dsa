## problem 1: dutch national flag
i
___________
0,0,2,1,1,2

  i
___________
0,0,2,1,1,2

    i
___________
0,0,1,1,2,2

      i
___________
0,0,1,1,2,2

        i
___________
0,0,1,1,2,2

          i
___________
0,0,1,1,2,2

solution: once i and two's index cross, the iteration should stop

## problem 2: binary search on 2d matrix

1. do a binary search on each row
2. before performing bsearch, check the bounds

## problem 3: serialize and deserialize binary search tree

### approach 1 (wrong)
1. just store inorder and preorder traversal of a tree
   "1,2,3,4;1,3,2,4"
2. construct tree from inorder and preorder traversal
    - now parse inorder and preorder traversal first - (done)

how do we construct tree from inorder and preorder list

with inorder, we can know which element are to the left, which are to the right.
How ??

say, inorder traversal is 2, 1, 4, 3, 5
then suppose, we are processing 1, then we know [2] is to the left of one
and [4, 3, 5] is to the right of one (4, 3, 5) is a right subtree
while (2) is a left subtree

from inorder, we maintain a idx map. We process preorder elements

my method breaks, because my method relies on the assumption that all node
values are unique, which isn't always the case.

### approach 2 
1. just do preorder traversal, if values are empty, just store them
as "N"
2. while deserializing start from the preorder traversal
do : build root, then build(root.left), build(root.right) and for each new dfs
we iterate over the values

### problem 4: flatten 2d vector 

- I used a very simple approach of using auxiliary space. Simply flatten the array
by constructing a new 1d array.
- Better approach is to check the bounds and move accordingly, use row and col
index , change col to 0 and move to new row at the end of column

### problem 5: happy number

create a helper function to sum the square of digits. And, keep checking if the
happy number is 1. If we visit the same number again, that means the number
doesn't reduce to 1 and we return false.

### problem 6: number of trailing zeros

trailing zeros means 10^(n) i.e 2^n * 5^n (5 is the limit in our case)
for any n from 1 to 10000. The ans is
n // (5**(1 to 5))

## problem 7: excel sheet number
this is fairly easy map each number to digit and use base 26

## problem 8: power of x, n
simple linear approach is pretty easy
p(x, n) = x * p(x, n - 1)

but we can do much better
p(x, n) = p(x * x, n // 2) if x is even
        = x * p (x * x, n // 2) if x is odd
base case: n = 0 return 1

## problem 9: todo: divide two integers

## problem 10: find the celebrity
idea is to minimize the call to knows(i, j)
brute force solution: check in a loop for i in range(0, n) , check if i is
celebrity, but this is 0(n^2)

We can do much better, we can find the candidate in a single pass

let's say a knows b , this means a can't be the candidate

so, we start with the candidate 0
if the candidate(0, 1) is true, now 1 becomes the candidate, since 0 knows and
by definition isn't a celebrity

at the end we have a celebrity candidate, and we check if all the other
candidates know him and he doesn't know anyone

## problem 11: Swap node pairs
a->b->c->d
a->next->b.next
b->next->a
a->b->c->d
a->c->d

## problem 12: Search BST
standard bst problem

## problem 13: Pascal's Triangle
1 f(0,0) = 1
1 1 f(1, 0) = 1, f(1,1)
1 2 1
1 3 3 1

f(r, c) = f(r-1, c-1) + f(r-1, c)

## problem 14: todo: kth symbol in grammar
