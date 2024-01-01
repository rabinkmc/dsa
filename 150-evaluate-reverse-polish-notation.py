from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = None
        for token in tokens:
            if token.isdigit() or (token[0]=="-" and token[1:]):
                stack.append(int(token))
            else:
                a = stack.pop()
                b = stack.pop()
                if token == "*":
                    result = b * a
                elif token == "/":
                    result = int(b/a)
                elif token == "-":
                    result = b - a
                else:
                    result = b + a
                stack.append(result)
                print(result)
        return stack[-1]

tokens = ["4","13","5","/","+"]
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
#tokens = ["3", "-4", "+"]
ans = Solution().evalRPN(tokens)
print(ans)
