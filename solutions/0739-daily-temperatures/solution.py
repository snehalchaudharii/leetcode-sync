class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        n= len(temperatures)
        result= [0]*n
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_val= stack.pop()
                result[prev_val] = i - prev_val
            stack.append(i)
        return result








        # brute force
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if temperatures[j]> temperatures[i]:
        #             result[i]= j - i
        #             break
        # return result
