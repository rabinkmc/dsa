from collections import defaultdict
from typing import List
from collections import deque


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = {}
        indegrees = {}
        for word in words:
            n = len(word)
            for i in range(n):
                ch1 = word[i]
                if ch1 not in indegrees:
                    indegrees[ch1] = 0
                if ch1 not in graph:
                    graph[ch1] = set()
                if i == n - 1:
                    continue

                ch2 = word[i + 1]
                if ch2 not in indegrees:
                    indegrees[ch2] = 0

                if ch1 == ch2:
                    continue

                if ch2 not in graph:
                    graph[ch2] = set()

                if ch2 in graph[ch1]:
                    continue
                else:
                    graph[ch1].add(ch2)
                    indegrees[ch2] += 1
        q = deque()
        for node in indegrees:
            if indegrees[node] == 0:
                q.append(node)

        ans = []
        while q:
            node = q.popleft()
            ans.append(node)
            for adj in graph[node]:
                indegrees[adj] -= 1
                if indegrees[adj] == 0:
                    q.append(adj)
            print(q)

        if len(indegrees) == len(ans):
            return "".join(ans)
        return ""


words = ["wrt", "wrf", "er", "ett", "rftt"]
words = ["z", "x"]
ans = Solution().alienOrder(words)
print(ans)
