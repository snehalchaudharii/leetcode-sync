class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        freq={}
        count=0
        for num in nums:
            count += freq.get(num-k, 0)
            count += freq.get(num+k, 0)
            freq[num] = freq.get(num, 0)+1
        return count


        # count=0
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if abs(nums[i]-nums[j])==k:
        #             count+=1
        # return count
