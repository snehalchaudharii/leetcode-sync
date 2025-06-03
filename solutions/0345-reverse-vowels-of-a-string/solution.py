class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels= {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}
        s = list(s)
        left=0
        right= len(s)-1

        while left< right:
            if s[left] in vowels and s[right]in vowels:
                s[left], s[right]= s[right], s[left]
                left+=1
                right-=1

            elif s[left] not in vowels:
                left+=1
            elif s[right] not in vowels:
                right-=1
        
        return ''.join(s)




        # vowels= {'a','e','i','o','u','A','E','I','O','U'}
        # s_list= list(s)
        # left=0
        # right= len(s)-1

        # while left<right:
        #     if s_list[left] not in vowels:
        #         left+=1
        #     elif s_list[right] not in vowels:
        #         right-=1
        #     else:
        #         s_list[left], s_list[right] = s_list[right], s_list[left]
        #         left+=1
        #         right-=1
        # return ''.join(s_list)
       
