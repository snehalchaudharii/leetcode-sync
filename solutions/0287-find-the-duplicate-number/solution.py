class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

# using slow fast approach # TC O(n) SC O(1)

        slow= nums[0]
        fast= nums[0]
       
        while True:
             slow= nums[slow]
             fast= nums[nums[fast]]
             if slow == fast:
                break
        slow= nums[0]
        while (slow!=fast):
             slow= nums[slow]
             fast= nums[fast]
        return slow

        # TC O(n) SC O(n)
        # freq={}
        # for num in nums:
        #     if num in freq:
        #         return num
        #     freq[num]= freq.get(num, 0)+1
        
