#include <stdlib.h>
#include <stdio.h>

struct TreeNode {
        int val;
        struct TreeNode *left;
        struct TreeNode *right;
};

struct TreeNode *new_node(int val) {
    struct TreeNode *node = malloc(sizeof(struct TreeNode));
    node->val = val;
    node->left = NULL;
    node->right = NULL;
    return node;
}

struct TreeNode *insert(struct TreeNode *root, int val) {
    if (!root) {
        return new_node(val);
    }
    struct TreeNode *curr = root;
    struct TreeNode *parent = NULL;
    while (curr) {
        parent = curr;
        if (val < curr->val) {
            curr = curr->left;
        } else {
            curr = curr->right;
        }
    }
    if (val < parent->val) {
        parent->left = new_node(val);
    } else {
        parent->right = new_node(val);
    }
    return root;
}

struct TreeNode *min_node(struct TreeNode *node) {
    while (node->left) {
        node = node->left;
    }
    return node;
}

struct TreeNode *deleteNode(struct TreeNode *root, int key) {
    if (!root) return NULL;
    if (key < root->val) {
        root->left = deleteNode(root->left, key);
    } else if (key > root->val) {
        root->right = deleteNode(root->right, key);
    } else {
        if (!root->right) {
            struct TreeNode *l = root->left;
            free(root);
            return l;
        }
        if (!root->left) {
            struct TreeNode *r = root->right;
            free(root);
            return r;
        }
        struct TreeNode *succ = min_node(root->right);
        root->val = succ->val;
        root->right = deleteNode(root->right, succ->val);
    }
    return root;
}

void pprint(struct TreeNode *node) {
    if (!node) return;
    printf("%d->", node->val);
    pprint(node->left);
    pprint(node->right);
}

int main() {
    struct TreeNode *root = insert(NULL, 5);
    insert(root, 3);
    insert(root, 6);
    insert(root, 2);
    insert(root, 4);
    insert(root, 7);
    pprint(root);
    printf("\n");
    deleteNode(root, 7);
    pprint(root);
    return 0;
}
