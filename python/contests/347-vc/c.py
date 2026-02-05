class Solution:
    def minimumCost(self, s: str) -> int:
        n = len(s)
        mid = n // 2 + ( n % 2 == 1)
        def furthest_targets(target):
            i = 0 
            left, right = None, None
            while i < mid:
                if s[i] == target:
                    left = i
                i = i + 1
            j = n - 1
            while j >= mid:
                if s[j] == target:
                    right = j 
                j = j - 1
            return left, right

        l0, r0 = furthest_targets("0") # trying to change to 1
        l1 , r1 = furthest_targets("1") # trying to change to 0

        def left_cost(l):
            if l is None:
                return 0
            cost = l + 1
            l = l - 1
            while l >= 0:
                if s[l] != s[l+1]:
                    cost += l + 1
                l -= 1
            return cost

        def right_cost(r):
            if r is None:
                return 0
            cost = n - r
            r = r + 1
            while r < n:
                if s[r] != s[r-1]:
                    cost += n - r
                r += 1
            return cost

        zero_ans = left_cost(l0) + right_cost(r0) 
        one_ans = left_cost(l1) + right_cost(r1) 
        return min(zero_ans, one_ans)

# s = "0011"
# ans = Solution().minimumCost(s)
# assert ans == 2
        
s = "01"
ans = Solution().minimumCost(s)
print(ans)
# assert ans == 9
