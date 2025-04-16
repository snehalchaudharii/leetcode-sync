class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        freqS= {}
        freqT= {}

        if len(s)!= len(t):
            return False
        
        for charS, charT in zip(s, t):
            if charS not in freqS and charT not in freqT:
                freqS[charS]= charT
                freqT[charT]= charS
            elif freqS.get(charS) != charT or freqT.get(charT)!=charS:
                return False
        return True
