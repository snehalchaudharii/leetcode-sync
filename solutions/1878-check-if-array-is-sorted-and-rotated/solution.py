class Solution:
    def check(self, nums: List[int]) -> bool:
        count_dec=0
        n= len(nums)
        for i in range(n):
            if nums[i]> nums[(i+1)%n]:
                
                count_dec+=1
            
            if count_dec> 1:
                return False
        return True
