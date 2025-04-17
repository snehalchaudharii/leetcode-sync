class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s)== sorted(t) TC- NlogN

# TC == O(n)
        if len(s)!= len(t):
            return False
        freq={}
        for i in range(len(s)):
# It adds 1 to the count of s[i] in the dictionary freq.
# If s[i] is not already in freq, it initializes freq[s[i]] to 0 before adding 1.
            freq[s[i]]= freq.get(s[i], 0) + 1
            freq[t[i]]= freq.get(t[i], 0) - 1
        return all( value== 0 for value in freq.values())


