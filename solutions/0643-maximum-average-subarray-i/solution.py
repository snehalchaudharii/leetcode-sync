class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        curr= sum(nums[:k])
        max_sum= curr

        for right in range(k, len(nums)):
            curr= curr + nums[right] - nums[right-k]
            max_sum= max(max_sum, curr)
        
        return max_sum/k
