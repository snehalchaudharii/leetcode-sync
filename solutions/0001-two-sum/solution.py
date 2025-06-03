class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq={}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in freq:
                return [i, freq[complement]]
            freq[num]=i
        return []



        # mp={}
        # for index, num in enumerate(nums):
        #     complement= target-num

        #     if complement in mp:
        #         return [mp[complement], index]
        #     mp[num]=index
        # return []


            
