class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left=0
        right= int(c**0.5)

        while left<= right:
            current_Sum= left**2 + right**2

            if current_Sum == c:
                return True
            elif current_Sum < c:
                left+=1
            else:
                right-=1
        return False
        
