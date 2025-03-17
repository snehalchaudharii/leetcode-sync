class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot= -1
        n= len(nums)
        # to find the pivot means the number from the right side which is smaller than its next number i.e 1,2,3,6,5,4 in this array 3 is the pivot number
        for i in range(n-2, -1, -1):
            if nums[i]< nums[i+1]:
                pivot= i
                break
        # if pivot not find and is --1 simple return array in smaller order
        if pivot==-1:
            nums.reverse()
            return
        
        # to find the larger element after pivot
        for i in range(n-1, pivot, -1):
            if nums[i]>nums[pivot]:
                nums[i], nums[pivot]=nums[pivot], nums[i]
                break
        
        # to reverse remaining elemnet after pivot
        left= pivot+1
        right=n-1
        while(left<right):
            nums[left], nums[right]= nums[right], nums[left]
            left+=1
            right-=1
        
