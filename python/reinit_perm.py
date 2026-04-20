class Solution:
    def reinitializePermutation(self, n: int) -> int:
        perm = list(range(n))
        orig = perm[:]
        temp = []
        for i in range(n):
            if i % 2 == 0:
                temp.append(perm[i // 2])
            else:
                temp.append(perm[n // 2 + (i - 1) // 2])
        perm = temp
        if perm == orig:
            return 1
        ops = 1
        while perm != orig:
            ops += 1
            temp = []
            for i in range(n):
                if i % 2 == 0:
                    temp.append(perm[i // 2])
                else:
                    temp.append(perm[n // 2 + (i - 1) // 2])
            perm = temp

        return ops


n = 6
ans = Solution().reinitializePermutation(n)
print(ans)
