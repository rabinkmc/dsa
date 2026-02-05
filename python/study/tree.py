"""
Binary tree 1

objective:

build(X) - n
get_at(i) - logn
set_at(i) - logn
insert_first(x) - logn
delete_first(x) - logn
insert_last(x) - logn 
delete_last(x) - logn
insert_at(i, x) - logn
"""


"""
Binary Trees
- are pointer based data structure with three pointers per node
- node representation: node. { item, parent, left, right}

Example: 
   A
  B C
 D E
F
"""

"""
Terminology 
- The root of a tree has bo parent
- The leaf of a tree has no children
- Define depth(X) of node X in a tree rooted at R to be length of path from X to R
- Define height(X) of node X to be max depth of any node in the subtree rooted at x
Idea: Design operations to run in O(h) time for root height h, and maintain h = O(logn)
- A binary tree has an inherent order: its traversal order
    * every node in the node<X>'s left subtree is before <X>
    * every node in the node<X>'s right subtree is after <X>

-  List node in traversal order via a recurisve algorithm start at root
    * Recursively list left subtree, list self, then recursively list right subtree 
    * Runs in 0(n) time, since O(1) work is done to list each node
"""


class TreeNode:
    def __init__(self, item, left=None, right=None, parent=None):
        self.item = item
        self.left = left
        self.right = right
        self.parent = parent

    def traverse(self, traversal_list=[]):
        if self.left:
            self.left.traverse(traversal_list)
        traversal_list.append((self.item))
        if self.right:
            self.right.traverse(traversal_list)
        return traversal_list

    def __str__(self):
        return str(self.item)

    def find_first(self):
        """
        while x has left child, recusively return the first node in the left subtree
        otherwise x is the first node
        """
        node = self
        while node and node.left:
            node = node.left
        return node

    def find_last(self):
        node = self
        while node and node.right:
            node = node.right
        return node

    def successor(self):
        """
        If x has right child, return first of right subtree
        otherwise, return the lowest ancestor of X which is in its left subtree
        """
        if self.right:
            return self.right.find_first()
        node = self
        while node.parent and (node is node.parent.right):
            node = node.parent
        return node.parent

    def predecessor(self):
        """
        If x has left child, return last of left subtree
        otherwise, return the lowest ancestor of X which is in its right subtree
        """
        if self.left:
            return self.left.find_last()
        node = self
        while node and (node is node.parent.left):
            node = node.parent
        return node.parent

    def insert_before(self, new):
        predecessor = self
        if self.left:
            predecessor = self.left.find_last()
            predecessor.right, new.parent = new, predecessor
        else:
            predecessor.left, new.parent = new, predecessor
        return new

    def insert_after(self, new):
        successor = self
        if self.right:
            successor = self.right.find_first()
            successor.left, new.parent = new, successor
        else:
            successor.right, new.parent = new, successor
        return new

    def delete(self):
        if self.left or self.right:
            B = self.predecessor() if self.left else self.successor()
            self.item, B.item = B.item, self.item
            B.delete()
        if self.parent:
            if self.parent.left == self:
                self.parent.left = None
            else:
                self.parent.right = None
        return self


a = TreeNode("A")
b = TreeNode("B", parent=a)
c = TreeNode("C", parent=a)
d = TreeNode("D", parent=b)
e = TreeNode("E", parent=b)
f = TreeNode("F", parent=d)

a.left = b
a.right = c
b.left = d
b.right = e
d.left = f

a.insert_after(TreeNode("G"))
a.insert_before(TreeNode("H"))
f.insert_after(TreeNode("I"))
j = f.insert_before(TreeNode("J"))
j.delete()
# print(a.traverse())
a.delete()

def build(X):
    def build_subtree(X, i, j):
        m = (i + j)//2
        root = TreeNode(X[m])
        if i < m:
            root.left = build_subtree(X, i, m - 1)
            root.left.parent = root
        if m < j:
            root.right = build_subtree(X, m+1, j)
            root.right.parent = root
        return root
    return build_subtree(X, 0, len(X) - 1)

Trees = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]

root = build(Trees)
print(root.traverse())

