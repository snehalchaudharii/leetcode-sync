class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x<0 else 1
        reverse= 0
        number= abs(x)
        while number:
            reverse= (reverse*10)+ (number%10)
            number//=10
        
            if reverse < -2**32 or reverse > 2**31:
                return 0
        return reverse*sign

        
