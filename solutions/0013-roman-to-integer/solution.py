class Solution:
    def romanToInt(self, s: str) -> int:
        dictval={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        sum=0
        for i in range(len(s)-1):
            if dictval[s[i]]< dictval[s[i+1]]:
    # If its value is less than the next character’s value, subtract it (handles cases like "IV").
                sum -= dictval[s[i]]
            else:
                sum +=dictval[s[i]]

        # After the loop, add the last character’s value separately
        sum += dictval[s[-1]]
        
        return sum
        
