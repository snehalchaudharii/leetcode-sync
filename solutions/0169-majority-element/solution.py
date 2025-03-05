class Solution:
    def majorityElement(self, nums: List[int]) -> int:
   
        # Brute force approach which will give time limit exceeded error
        #time complexity o(n2)

        # for num in nums:
        #     freq=0
        #     for i in nums:
        #         if num == i:
        #             freq+=1
            
        #     if freq > (len(nums)//2):
        #         return num

        # using sorting method
        #time complexity o(nlogn) + o(n)

        # nums.sort()
        # freq=1
        # for i in range(len(nums)):
        #     if nums[i]==nums[i-1]:
        #         freq+=1
        #     else:
        #         freq=1
        #     if freq > (len(nums)//2):
        #         return nums[i]
            
        # return -1

        # Moore's voting algorithm otimize apporoach
        freq=0
        storage=0
        for i in range(len(nums)):
            if freq==0:
                storage= nums[i]
            if storage == nums[i]:
                freq+=1
            else:
                freq-=1
        count=0
        for num in nums:
            if num == storage:
                count+=1
        if count > (len(nums)//2):
            return storage
        else: 
            return -1

        return storage



                   
        

