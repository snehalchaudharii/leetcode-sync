class Solution:
    def reverseWords(self, s: str) -> str:
        # SC= o(n)
        # s= s.strip()
        # words= s.split()
        # words.reverse()
        # return ' '.join(words)

        # SC= O(1) in place modification
        s= list(s)
        self.reverse(s, 0, len(s)-1)
        start=0
        for i in range(len(s)):
            if s[i]== " ":
                self.reverse(s, start, i-1)
                start= i+1
            
        self.reverse(s, start, len(s)-1)

        result= "".join(s).strip()
        return " ".join(result.split())

    def reverse(self, s, start, end):
        while start<end:
            s[start], s[end]= s[end], s[start]
            start+=1
            end-=1


