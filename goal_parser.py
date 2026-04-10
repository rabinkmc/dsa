class Solution:
    def interpret(self, command: str) -> str:
        n = len(command)

        out = []
        i = 0
        while i < n:
            if command[i] == "G":
                out.append("G")
                i += 1
            elif i + 1 < n and command[i : i + 2] == "()":
                out.append("o")
                i += 2
            elif i + 3 < n and command[i : i + 4] == "(al)":
                out.append("al")
                i += 4

        return "".join(out)


command = "(al)G(al)()()G"
ans = Solution().interpret(command)
print(ans)
