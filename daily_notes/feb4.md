## previous todos

1. design hashmap - done
2. design hashset - done
3. delete node in a bst 

## today's target
get very comfortable with binary search trees

-  **insertion** is just like search, keep searching for insertion point until curr
   is null and during this process, keep track of parent pointer.

   now compare the target value with parent node and put the node accordingly to
   the left or the right of parent.

- **predecessor and successor**
  
  **predecessor: is the greatest value smallest than the current node**
  **successor: is the smallest value greater than the current node**

  let's first look at successor:
  1. there are two cases, the current node has a left subtree
     if left subtree exists, then the successor is the right most node of that
  subtree
  2. this second case is what always trips me. Actually this is simpler than I
     thought especially in BST. This is the same operation as I do in binary
  search for the case of finding value just smaller than the target value.
     ```c
     Node *successor(Node *root, int key) {
         Node *succ = NULL;
         Node *curr = root;
         while (curr) {
             if (curr->val > val) {
                 // this is a candidate answer
                 succ = curr;
                 curr = curr->left;
             } else {
                 curr = curr->right;
             }
         }
         return succ;
     }
     ```

     Similarly the predecessor has the exact symmetric code
- **Deletion**
  Deletion has 3 cases.

  1. leaf node - just remove (easy case)
  2. one child - replace node with child, and delete the node (now at leaf)
  3. two children - swap with successor, then delete successor

## 
