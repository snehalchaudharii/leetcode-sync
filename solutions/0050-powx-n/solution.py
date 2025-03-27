class Solution:
    def myPow(self, x: float, n: int) -> float:
        # using binary exponentioal form basically squareing
        result=1
        bindaryForm = n
        if bindaryForm==0:
            return 1.0
        if x==0:
            return 0.0
        if x==1: 
            return 1.0
        if x== -1 and bindaryForm%2==0:
            return 1.0
        if x== -1 and bindaryForm%2!=0:
            return -1.0

        if bindaryForm <0:
            x= 1/x
            bindaryForm= -bindaryForm
        
        while bindaryForm >0:
            if bindaryForm%2 == 1:
                result *= x
            x*=x
            bindaryForm= bindaryForm//2
        
        return result
 
