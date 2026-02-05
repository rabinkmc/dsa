"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from typing import Optional
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        queue = deque([node])
        clones = {}
        clones[node.val] = Node(node.val)

        while queue:
            curr = queue.popleft()
            cur_clone = clones[curr.val]
            for next_node in curr.neighbors:
                if next_node.val not in clones:
                    clones[next_node.val] = Node(next_node.val)
                    queue.append(next_node)
                cur_clone.neighbors.append(clones[next_node.val])
        return clones[node.val]
