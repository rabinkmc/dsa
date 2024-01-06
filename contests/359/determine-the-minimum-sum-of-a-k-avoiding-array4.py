class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        count = 0 
        i = 1
        ans = []
        comp = dict()
        total = 0
        while count < n and i < k:
            if i not in comp:
                total += i
                count = count + 1
                comp[k-i] = i
            i = i + 1

        while count < n:
            total += i
            i = i + 1
            count += 1
            
        return total

n = 5
k = 4
print(Solution().minimumSum(n, k))
        
