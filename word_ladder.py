from typing import List
from collections import deque, defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        if not wordList:
            return 0
        q = deque()
        graph = defaultdict(list)
        L = len(beginWord)
        for word in wordList:
            for i in range(L):
                tmp = word[:i]  + "*" + word[i+1:]
                graph[tmp].append(word)
        q.append(beginWord)
        level = 1
        visited = {beginWord}
        while q:
            sz = len(q)
            for _ in range(sz):
                node = q.popleft()
                for i in range(L):
                    tmp = node[:i] + "*" + node[i+1:]
                    for word in graph[tmp]:
                        if word == endWord:
                            return level + 1
                        if word in visited:
                            continue
                        visited.add(word)
                        q.append(word)
            level += 1

        return 0

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
ans = Solution().ladderLength(beginWord, endWord, wordList)
print(ans)
        
