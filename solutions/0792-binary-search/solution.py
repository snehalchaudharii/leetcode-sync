class Solution:
    def binSearch(self, nums, target, start, end):
        if start<= end:
            mid= start + (end-start)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] >= target:
                return self.binSearch(nums, target, start, mid-1)
            else:
                return self.binSearch(nums, target, mid+1, end)
        return -1
    def search(self, nums: List[int], target: int) -> int:
        return self.binSearch(nums, target, 0, len(nums)-1)
