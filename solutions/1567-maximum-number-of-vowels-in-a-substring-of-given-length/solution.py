class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel= {'a','e','i','o','u'}
        left=0
        curr=0
        max_v=0
        for right in range(len(s)):
            if s[right] in vowel:
                curr+=1
            if (right-left+1)==k:
                max_v= max(max_v, curr)
                if s[left] in vowel:
                    curr-=1
                left+=1
        return max_v
