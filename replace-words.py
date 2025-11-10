from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_root = False

    def __str__(self):
        return f"{self.children}->{self.is_root}"


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_root = True

    def findPrefix(self, word: str) -> str:
        curr = self.root
        res = ""
        for ch in word:
            if ch not in curr.children:
                break
            if curr.children[ch].is_root:
                return res + ch
            else:
                res += ch
            curr = curr.children[ch]
        return ""


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split()
        trie = Trie()
        for key in dictionary:
            trie.insert(key)

        res = []
        for word in words:
            pre = trie.findPrefix(word)
            if not pre:
                res.append(word)
            else:
                res.append(pre)

        return " ".join(res)


dictionary = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
print(Solution().replaceWords(dictionary, sentence))
