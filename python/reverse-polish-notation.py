from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ["*", "/", "-", "+"]:
                stack.append(int(token))
                continue

            b = stack.pop()
            a = stack.pop()
            if token == "*":
                stack.append(a*b)
            elif token == "/":
                if a * b < 0:
                    stack.append(-(abs(a) // abs(b)))
                else:
                    stack.append(a // b)
            elif token == "-":
                stack.append(a-b)
            elif token == "+":
                stack.append(a+b)
            print(stack)
        return stack[0]
        
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(Solution().evalRPN(tokens))
