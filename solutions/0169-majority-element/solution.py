class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element = None
        count = 0
        
        # Step 1: Find the potential majority element
        for num in nums:
            if count == 0:
                element = num
            count += (1 if num == element else -1)
        
        # Step 2: Return the potential majority element
        # No verification step is needed since the problem guarantees that a majority element always exists.
        return element

