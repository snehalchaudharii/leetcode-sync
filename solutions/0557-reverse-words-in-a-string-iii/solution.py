class Solution:
    def reverseWords(self, s: str) -> str:
        s= list(s)
        n= len(s)

        def reverse(left, right):
            while left<right:
                s[left], s[right]=s[right], s[left]
                left+=1
                right-=1
        start=0
        for end in range(n+1):
            if end==n or s[end]==" ":
                reverse(start, end-1)
                start= end+1
        return "".join(s)
