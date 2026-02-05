from typing import List
from collections import deque


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        options = {
            "A": ["C", "G", "T"],
            "C": ["A", "G", "T"],
            "G": ["A", "C", "T"],
            "T": ["A", "C", "G"],
        }

        def next_nodes(gene):
            temp = []
            for i, ch in enumerate(gene):
                for mutation in options[ch]:
                    gene_string = gene[:i] + mutation + gene[i + 1 :]
                    if gene_string in bank:
                        temp.append(gene_string)
            return temp

        queue = deque([startGene])
        visited = set()
        visited.add(startGene)
        step = 0
        while queue:
            qs = len(queue)
            for _ in range(qs):
                node = queue.popleft()
                if node == endGene:
                    return step
                for next_node in next_nodes(node):
                    if next_node in visited:
                        continue
                    queue.append(next_node)
                    visited.add(next_node)
            step += 1

        return -1


print(
    Solution().minMutation(startGene="AACCGGTT", endGene="AACCGGTA", bank=["AACCGGTA"])
)
