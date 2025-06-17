class Solution:
    def largestOddNumber(self, num: str) -> str:
        longest= ''
        i=0
        res=''
        while i < len(num):
            if num[i].isdigit():
                res+=num[i]
                i+=1
            else:
                i+=1
            if int(res[-1]) % 2 == 1 and len(res)> len(longest):
                longest = res
        return longest
            


