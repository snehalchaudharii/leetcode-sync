class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kadan's algorithm
        currentSum= 0
        maxSum= float("-inf")
        for num in nums:
            currentSum += num
            maxSum= max(maxSum, currentSum)
            if currentSum < 0:
                currentSum = 0
            
        return maxSum
            

# Brute force apporach which will give time limit exceeded error
        # maxSum= float('-inf')
        # for start in range(len(nums)):
        #     currentSum=0
        #     for end in range(start, len(nums)):
        #         currentSum += nums[end]
        #         maxSum = max(currentSum, maxSum)
        # return maxSum
        

