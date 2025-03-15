class Solution:
    def isValid(self, nums: List[int], maxallowedpages:int, k: int) -> int:
        student=1
        pages=0

        for i in range(len(nums)):
            if nums[i]>maxallowedpages:
                return False
            if pages+ nums[i]<= maxallowedpages:
                pages += nums[i]
            else:
                student+=1
                pages = nums[i]
            
            if student > k:
                return False
        return True

    def splitArray(self, nums: List[int], k: int) -> int:
        total_sum = 0
        if k> len(nums):
            return -1
        start=0
        end= sum(nums)
        ans=-1
        while (start<=end):
            mid= start + (end-start)//2
            if self.isValid(nums, mid, k):
                ans= mid
                end= mid-1
            else:
                start= mid+1
        return ans
        
