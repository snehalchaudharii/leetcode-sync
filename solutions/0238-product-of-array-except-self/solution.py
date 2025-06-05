class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force approach Time Limit Exceeded
        # ans=[]
        # for i in range(len(nums)):
        #     prod=1
        #     for j in range(len(nums)):
        #         if i!=j:
        #             prod *= nums[j]
        #     ans.append(prod)
        # return ans

        # Optimized method by calculating prefix and sufficx before hand TC & SC O(n)
        # n= len(nums)
        # ans= [1]*n
        # # to calculate prefix
        # prefix=[1]*n
        # for i in range(1,n):
        #     prefix[i]= prefix[i-1]*nums[i-1]
        
        # # to calculate suffix
        # suffix=[1]*n
        # for i in range(n-2, -1, -1):
        #     suffix[i]= suffix[i+1]*nums[i+1]
        
        # for i in range(len(nums)):
        #     ans[i]= prefix[i]*suffix[i]
        
        # return ans

        # To save the space
        res= [1] * len(nums)

        prefix=1

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix= 1

        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res

        
