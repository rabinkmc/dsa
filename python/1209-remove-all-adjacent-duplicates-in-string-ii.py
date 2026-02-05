class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # maintain a stack of characters with their count once, the count reaches 3 pop that character from the stack
        stack = []
        for ch in s:
            if stack and ch == stack[-1][0]:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([ch, 1])
        res = []
        for ch, count in stack:
            res = res + [ch]*count
        return "".join(res)
                

print(Solution().removeDuplicates(s = "deeedbbcccbdaa", k = 3))
