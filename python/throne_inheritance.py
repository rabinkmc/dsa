from typing import List


class Node:
    __slots__ = ("name", "children", "alive")

    def __init__(self, childName):
        self.name = childName
        self.children = []
        self.alive = True


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.root = Node(childName=kingName)
        self.nodes_map = {kingName: self.root}
        self._cache = None

    def birth(self, parentName: str, childName: str) -> None:
        child = Node(childName=childName)
        parent = self.nodes_map[parentName]
        parent.children.append(child)
        self.nodes_map[childName] = child
        self._cache = None

    def death(self, name: str) -> None:
        node = self.nodes_map[name]
        node.alive = False
        self._cache = None

    def getInheritanceOrder(self) -> List[str]:
        if self._cache is not None:
            return self._cache
        order = []

        def dfs(node):
            if node.alive:
                order.append(node.name)
            for next_child in node.children:
                dfs(next_child)

        dfs(self.root)
        self._cache = order
        return order


# Your ThroneInheritance object will be instantiated and called as such:

t = ThroneInheritance("King")
t.birth("King", "Andy")
t.birth("King", "Bob")
t.birth("King", "Catherine")
t.birth("Andy", "Matthew")
t.birth("Bob", "Alex")
t.birth("Bob", "Asha")
t.death("Bob")
print(t.getInheritanceOrder())

# obj.death(name)
# param_3 = obj.getInheritanceOrder()
