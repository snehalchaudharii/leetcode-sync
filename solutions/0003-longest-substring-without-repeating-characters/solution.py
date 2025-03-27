class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count=0
        longstr= set()
        left=0
        right=0
        while right< len(s):
            if s[right] not in longstr:
                longstr.add(s[right])
                count= max(count, right-left+1)
                right+=1
            else:
                longstr.remove(s[left])
                left+=1
        
        return count

            

