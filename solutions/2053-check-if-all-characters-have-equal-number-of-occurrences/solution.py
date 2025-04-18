class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq={}
        for i in s:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        
        return len(set(freq.values()))==1

