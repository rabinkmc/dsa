from collections import Counter


class Solution:
    def countWordOccurrences(self, chunks: list[str], queries: list[str]) -> list[int]:
        def is_letter(ch):
            return ord(ch) >= ord("a") and ord(ch) <= ord("z")

        st = "".join(chunks)
        n = len(st)
        words = []
        curr = []

        for i in range(n):
            ch = st[i]
            if is_letter(ch):
                curr.append(ch)
            elif ch == "-":
                if (
                    i > 0
                    and i + 1 < n
                    and is_letter(st[i + 1])
                    and is_letter(st[i - 1])
                ):
                    curr.append(ch)
                else:
                    words.append("".join(curr))
                    curr = []
            else:
                words.append("".join(curr))
                curr = []
        if curr:
            t = "".join(curr)
            words.append(t)
        counter = Counter(words)
        out = []
        for query in queries:
            out.append(counter[query])
        return out


chunks = ["hello wor", "ld hello"]
queries = ["hello", "world", "wor"]
chunks = ["a--b a-", "-c"]
queries = ["a", "b", "c"]


ans = Solution().countWordOccurrences(chunks, queries)
print(ans)
