class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet= set(nums)
        longest= 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length+=1
                
                longest = max(length, longest)
        return longest












        # res=0
        # store= set(nums)
        # for num in nums:
        #     streak=0
        #     curr= num
        #     while curr in store:
        #         streak+=1
        #         curr+=1
        #     res = max(res, streak)
        # return res
        # Time complexity: O(n) square
        # Space complexity: O(n)

