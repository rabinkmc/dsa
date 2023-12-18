class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch != "]":
                stack.append(ch)
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()
                num = ""
                while stack and stack[-1].isdigit():
                    num = num + stack.pop()
                stack.append(int(num) * substr)
        return "".join(stack)


# s1 = "3[a]2[bc]"
# out1 = [3, "a", 2, "bc"]
# out1 = "aaabcbc"
s2 = "3[a2[c]]"
# out2 = [3, "a2[c]"]
# out2 = [3, "acc"]
# out2 = "accaccacc"
# s3 = "2[abc]3[cd]ef"
print(Solution().decodeString(s2))
