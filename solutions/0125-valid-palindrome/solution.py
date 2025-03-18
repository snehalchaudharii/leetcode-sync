class Solution:
    def isPalindrome(self, s):
        # s= "".join(char.lower() for char in s if char.isalnum())
        # left=0
        # right= len(s)-1
        # while left< right:
        #     if s[left]!=s[right]:
        #         return False
        #     else:
        #         left+=1
        #         right-=1
        # return True

        left=0
        right= len(s)-1
        while left< right:
            if not s[left].isalnum():
                left+=1
                continue
            if not s[right].isalnum():
                right-=1
                continue
            if s[left].lower() != s[right].lower():
                return False
            else:
                left+=1
                right-=1
        return True
