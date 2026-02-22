from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_sentence = False
        self.hotness = 0
        self.sentence = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, sentence):
        curr = self.root
        for ch in sentence:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr =curr.children[ch]
        curr.is_sentence = True
        curr.sentence = sentence

    def prefix(self, prefix):
        curr = self.root
        for ch in prefix:
            if ch in curr.children:
                curr = curr.children[ch]
            else:
                return None
        return curr

    def descendants(self, prefix):
        root = self.prefix(prefix)
        if not root:
            return []
        res = list(prefix)
        answers = []
        def dfs(node):
            if node.is_sentence:
                answers.append(node.sentence)
            for child in node.children.values():
                dfs(child)
        dfs(root)
        return answers



class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.times = times
        self.tree = Trie()
        n = len(sentences)
        self.hotness = dict()
        for i in range(n):
            sentence = sentences[i]
            self.hotness[sentence] = times[i]
            self.tree.insert(sentence)
        self.current = []
        

    def input(self, c: str) -> List[str]:
        if c == '#':
            sentence = "".join(self.current)
            if sentence not in self.hotness:
                self.tree.insert(sentence)
                self.hotness[sentence] = 1
            else:
                self.hotness[sentence] += 1
            self.current = []
            return []
        self.current.append(c)
        prefix = "".join(self.current)
        sentences = self.tree.descendants(prefix)
        sentences.sort(key=lambda s: (-self.hotness[s], s))
        return sentences[:3]
        
sentences = ["i love you", "island", "iroman", "i love leetcode"]
times = [5, 3, 2, 2]
obj = AutocompleteSystem(sentences, times)
print(obj.input("i"))
print(obj.input(" "))
print(obj.input("a"))
