class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq={}
        for s in magazine:
            freq[s]= freq.get(s, 0)+1
        for c in ransomNote:
            freq[c] = freq.get(c, 0)-1
            if freq[c]<0:
                return False
        return True
                
        
