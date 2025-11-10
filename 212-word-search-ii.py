from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

    def __str__(self):
        return f"{self.children}->{self.is_word}"


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])

        found = set()

        def dfs(r, c, node, path):
            if node.is_word:
                found.add(path)

            if r < 0 or r >= m or c < 0 or c >= n:
                return
            if board[r][c] not in node.children:
                return

            ch = board[r][c]
            board[r][c] = "#"
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(r + dr, c + dc, node.children[ch], path + ch)
            board[r][c] = ch

        trie = Trie()
        for word in words:
            trie.insert(word)

        for i in range(m):
            for j in range(n):
                dfs(i, j, trie.root, "")
        return list(found)


board = [
    ["o", "a", "a", "n"],
    ["e", "t", "a", "e"],
    ["i", "h", "k", "r"],
    ["i", "f", "l", "v"],
]

words = ["oath", "pea", "eat", "rain"]
print(Solution().findWords(board, words))
