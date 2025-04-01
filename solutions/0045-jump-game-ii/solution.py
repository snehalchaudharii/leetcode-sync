class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return 0
        jumps=0
        next_reach=0
        current_reach=0
        for i in range(len(nums)):
            if i>current_reach:
                jumps+=1
                current_reach=next_reach
            
            next_reach= max(next_reach, i+nums[i])

            if next_reach >= len(nums)-1:
                return jumps+1
        return jumps

        
