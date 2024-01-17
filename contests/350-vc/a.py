 # 2739. Total Distance Traveled
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        ans = 0
        while (mainTank >= 5):
            mainTank -= 5
            ans +=  5 * 10 
            mainTank += 1 if (additionalTank > 0) else 0
            additionalTank -= 1
        ans += mainTank * 10
        return ans

ans = Solution().distanceTraveled(mainTank = 50, additionalTank = 10)
print(ans)
        
