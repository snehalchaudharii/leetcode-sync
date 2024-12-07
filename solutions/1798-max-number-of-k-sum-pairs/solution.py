class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left=0
        right= len(nums)-1
        operation=0

        while left < right:
            currentSum= nums[left]+nums[right]
            if currentSum == k:
                operation+=1
                left+=1
                right-=1
            elif currentSum < k:
                left+=1
            else:
                right-=1
        return operation


