class Solution:
    def romanToInt(self, s: str) -> int:
        dictval={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        sum=0
        for i in range(len(s)-1):
            if dictval[s[i]]< dictval[s[i+1]]:
                sum -= dictval[s[i]]
            else:
                sum +=dictval[s[i]]

        if dictval[s[-1]]:
            sum +=dictval[s[-1]]
        
        return sum
        
