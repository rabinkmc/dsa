class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def f(row):
            if not row:
                return '0'

            res = []
            for ch in row:
                if ch == '0':
                    res.append('0')
                    res.append('1')
                else:
                    res.append('1')
                    res.append('0')
            return "".join(res)

        curr = ""
        for i in range(n):
            curr = f(curr)
        return int(curr[k-1])

n = 4
k = 2
ans = Solution().kthGrammar(n, k)
print(ans)
        
