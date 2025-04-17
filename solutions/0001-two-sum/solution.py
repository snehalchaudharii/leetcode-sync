class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp={}
        for index, num in enumerate(nums):
            complement= target-num

            if complement in mp:
                return [mp[complement], index]
            mp[num]=index
        return []


            
