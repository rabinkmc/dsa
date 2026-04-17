## the idea is simple create a simple string to
## represent the array null values are represented
## as N
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def pprint(node):
    if not node:
        return
    pprint(node.left)
    print(node.val, end="->")
    pprint(node.right)


class Codec:
    def serialize(self, root):
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                res.append("N")
                continue
            res.append(str(node.val))
            stack.append(node.right)
            stack.append(node.left)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        print(data)
        vals = iter(data.split(","))

        def dfs():
            val = next(vals)
            if val == "N":
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()


# Your Codec object will be instantiated and called as such:
ser = Codec()
one = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
four = TreeNode(4)
five = TreeNode(5)
one.left = two
one.right = three
three.left = four
three.right = five

print(ser.serialize(one))

# pprint(ser.deserialize(ser.serialize(one)))
# ans = deser.deserialize(ser.serialize(root))
