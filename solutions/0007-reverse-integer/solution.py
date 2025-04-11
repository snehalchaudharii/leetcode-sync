class Solution:
    def reverse(self, x: int) -> int:
        revnum = 0
        sign = 1 if x > 0 else -1
        x = abs(x)
        while x != 0:
            extractLast = x % 10
            if (revnum > (2**31) // 10 or revnum < (-2**31) // 10):
                return 0
            revnum = (revnum * 10) + extractLast
            x = x // 10
        return revnum * sign
        
       
           


        
