class Solution:
    def fib(self, n: int) -> int:
    #    prev, curr= 0, 1
    #    for i in range(n):
    #     prev, curr= curr, prev+curr
    #    return prev

        if n<=1:
            return n
        return self.fib(n-1) + self.fib(n-2)
