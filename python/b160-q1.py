def get_digit_repr(digit):
    if digit < 10:
        return str(digit)
    return chr(ord('A') + digit - 10)

class Solution:
    def concatHex36(self, n: int) -> str:
        square = n * n
        cube = n * n * n
        sstr = ""
        while square:
            digit = square % 16
            square = square // 16
            sstr = get_digit_repr(digit) + sstr

        cstr = ""
        while cube:
            digit = cube % 36
            cube = cube // 36
            cstr = get_digit_repr(digit) + cstr
        return sstr + cstr
        
