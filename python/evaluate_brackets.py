from typing import List


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        out = []
        i = 0
        n = len(s)
        out = []
        tmp = []
        VAR = 0
        LITERAL = 1
        while i < n:
            if s[i] == "(":
                if tmp:
                    out.append((LITERAL, "".join(tmp)))
                    tmp = []
                i += 1
                tmp = []
                while i < n and s[i] != ")":
                    tmp.append(s[i])
                    i += 1
                key = "".join(tmp)
                tmp = []
                out.append((VAR, key))
            else:
                tmp.append(s[i])
            i += 1
        if tmp:
            out.append((LITERAL, "".join(tmp)))

        knowledge_map = dict()
        for key, val in knowledge:
            knowledge_map[key] = val

        res = []
        for typ, val in out:
            if typ == LITERAL:
                res.append(val)
            else:
                txt = "?"
                if val in knowledge_map:
                    txt = knowledge_map[val]
                res.append(txt)

        return "".join(res)


s = "(name)is(age)yearsold"
knowledge = [["name", "bob"], ["age", "two"]]
ans = Solution().evaluate(s, knowledge)
print(ans)
