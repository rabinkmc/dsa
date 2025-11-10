from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree_level_order(arr, i=0):
    if i >= len(arr) or arr[i] is None:
        return None
    root = TreeNode(arr[i])
    root.left = build_tree_level_order(arr, 2 * i + 1)
    root.right = build_tree_level_order(arr, 2 * i + 2)
    return root


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        stack = []
        self.i = 0
        self.res = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            self.res.append(curr.val)
            curr = curr.right

    def next(self) -> int:
        ans = self.res[self.i]
        self.i += 1
        return ans

    def hasNext(self) -> bool:
        return self.i < len(self.res)


root = build_tree_level_order([7, 3, 15, None, None, 9, 20])
obj = BSTIterator(root)

for _ in range(5):
    print(obj.hasNext(), obj.next())
print(obj.hasNext())
