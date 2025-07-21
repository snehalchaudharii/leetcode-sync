class Solution:
    def checkDivisibility(self, n: int) -> bool:
        Dsum = 0
        Dproduct = 1
        total= 0
        Dlist = str(n)

        for num in Dlist:
            digit = int(num)
            Dsum += digit
            Dproduct *= digit
        total= Dsum + Dproduct

        if (n % total == 0) and ( total != 0 ):
            return True
        else:
            return False
            
            
            
