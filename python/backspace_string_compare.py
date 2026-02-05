# https://leetcode.com/problems/backspace-string-compare/


def backspace_string_compare(s: str, t: str) -> bool:
    new_s = []
    new_t = []
    for i in range(len(s)):
        if s[i] == '#':
            new_s.pop()
        else:
            new_s.append(s[i])

    for i in range(len(t)):
        if t[i] == '#':
            new_t.pop()
        else:
            new_t.append(t[i])
    
    return new_s == new_t


s = "ab#c"
t = "ad#c"

print(backspace_string_compare(s, t))
