from collections import defaultdict

class Solution:
    def maximumLength(self, s: str) -> int:
        indices = dict()
        occurence = defaultdict(int)
        for i, ch in enumerate(s):
            if ch not in indices:
                indices[ch] = [[i, i]]
            elif i - indices[ch][-1][1] == 1:
                indices[ch][-1][1] = i
            else:
                indices[ch].append([i, i])
            occurence[ch] += 1
        ans = -1
        for ch, idx in indices.items():
            if occurence[ch] < 3:
                continue
            diffs = [end - start + 1 for start, end in idx]
            diffs.sort()
            lmax = 0
            a = diffs[-1]
            b = diffs[-2] if len(diffs) >= 2 else -1
            c = diffs[-3] if len(diffs) >= 3 else -1
            if a == b == c:
                lmax = a
            elif a - b <= 1:
                lmax = a - 1
            else:
                lmax = a - 2
            ans = max(ans, lmax)
        return ans

        
s = "aaaabbbbbbaaaaa"
ans = maximumLength(s)
print(ans)


