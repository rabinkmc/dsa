class TrieNode:
    def __init__(self):
        self.children = {}
        self.data = 0

    def __str__(self):
        return f"{self.children}->{self.data}"


class MapSum:

    def __init__(self):
        self.root = TrieNode()

    def __str__(self):
        return str(self.root)

    def insert(self, key: str, val: int) -> None:
        curr = self.root
        for ch in key:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.data = val

    def search(self, prefix):
        curr = self.root
        for ch in prefix:
            if ch not in curr.children:
                return None
            curr = curr.children[ch]
        return curr

    def sum(self, prefix: str) -> int:
        subtree = self.search(prefix)
        if not subtree:
            return 0

        self.result = 0

        def dfs(node):
            if not node:
                return
            self.result += node.data
            for ch in node.children:
                dfs(node.children[ch])

        dfs(subtree)
        return self.result


# Your MapSum object will be instantiated and called as such:
obj = MapSum()
obj.insert("apple", 3)
print(obj.sum("app"))
# param_2 = obj.sum(prefix)
