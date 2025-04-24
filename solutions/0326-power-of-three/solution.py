class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==1:
            return True
        elif n%3 ==0 and n!=0:
            n=n//3
            return self.isPowerOfThree(n)
        return False



#         Time complexity: O(log(n))
# Space complexity: O(log(n))

