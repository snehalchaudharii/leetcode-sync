class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        prefixSum=0
        hashmap={0:1} # Initialize with 0 sum having frequency 1
        for num in nums:
            prefixSum += num

            if prefixSum-k in hashmap:
                count += hashmap[prefixSum-k]
            
            hashmap[prefixSum]= hashmap.get(prefixSum , 0)+1
        return count
            
