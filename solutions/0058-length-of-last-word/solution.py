class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # count=0
        # s= s.strip()
        # n= len(s)
        # for i in range(n-1, -1, -1):
        #     if s[i]!=" ":
        #         count+=1
        #     else:
        #         break
        # return count
        
        return len(s.strip().split()[-1])

