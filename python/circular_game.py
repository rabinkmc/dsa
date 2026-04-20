class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = list(range(1, n + 1))
        i = 0
        while len(arr) > 1:
            i = (i + k - 1) % len(arr)
            arr = arr[:i] + arr[i + 1 :]
        return arr[0]


n, k = 5, 2
ans = Solution().findTheWinner(n, k)
print(ans)
