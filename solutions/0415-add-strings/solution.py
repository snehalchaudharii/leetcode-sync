class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        p= len(num1)-1
        q= len(num2)-1
        result=[]
        carry=0

        while p>=0 or q>=0 or carry:
            digit1= int(num1[p]) if p>=0 else 0
            digit2 = int(num2[q]) if q>=0 else 0

            total= digit1 + digit2 + carry
            carry= total//10
            digit= total%10

            result.append(str(digit))

            p-=1
            q-=1
        
        return "".join(result[::-1])
