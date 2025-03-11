class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start=0
        end= len(nums)-1
        if len(nums)==1:
            return nums[0]

        while(start<=end):
            mid= start+ (end-start)//2

            if mid==0 and nums[0]!= nums[1]:
                return nums[mid]
            
            if (mid==len(nums)-1) and ((nums[len(nums)-1])!= (nums[len(nums)-2])):
                return nums[mid]

            if nums[mid-1]!=nums[mid]!=nums[mid+1]:
                return nums[mid]
            # for even array on both side of mid point
            if mid%2==0: 
                if nums[mid-1]==nums[mid]:
                    end= mid-1
                else:
                    start= mid+1
            else:
                if nums[mid-1]==nums[mid]:
                    start= mid+1
                else:
                    end= mid-1
        return -1


