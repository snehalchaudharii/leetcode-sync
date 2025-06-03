class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s)== sorted(t) TC- NlogN

# Still O(n) time and space, but avoids building two full dictionaries.
        freq={}

        if len(s)!= len(t):
            return False

        for ch in s:
            freq[ch]= freq.get(ch, 0)+1
        
        for ch in t:
            if ch not in freq:
                return False
            
            freq[ch]-=1

            if freq[ch]<0:
                return False
        return True



        # freqS={}
        # freqT={}
        # if len(s)!=len(t):
        #     return False
# It adds 1 to the count of s[i] in the dictionary freq.
# If s[i] is not already in freq, it initializes freq[s[i]] to 0 before adding 1.
        # for i in range(len(s)):
        #     freqS[s[i]]= freqS.get(s[i], 0)+1
        #     freqT[t[i]]= freqT.get(t[i], 0)+1       
        # return freqS == freqT



















