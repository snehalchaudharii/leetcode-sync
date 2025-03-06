class Solution:
    def myPow(self, x: float, n: int) -> float:
        # using binary exponentioal form basically squareing
        result=1

        if n==0:
            return 1.0
        if x==0:
            return 0.0
        if x==1: 
            return 1.0
        if x== -1 and n%2==0:
            return 1.0
        if x== -1 and n%2!=0:
            return -1.0

        if n<0:
            x= 1/x
            n= -n
        
        while n>0:
            if n%2 == 1:
                result *= x
            x*=x
            n= n//2
        
        return result
 
