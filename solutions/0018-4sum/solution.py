class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)
        
        for i in range(n - 3):  # Stop at n-3 to ensure 4 numbers
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates for i
                continue
            for j in range(i + 1, n - 2):  # Stop at n-2 for 3 numbers
                if j > i + 1 and nums[j] == nums[j - 1]:  # Skip duplicates for j
                    continue
                left = j + 1
                right = n - 1
                
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total < target:
                        left += 1
                    elif total > target:
                        right -= 1
                    else:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        # Skip duplicates for left
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        
                            
        return result

# TC nlogn + n^3






        # nums.sort()  # Sort the array
        # n = len(nums)
        # result = []

        # for i in range(n - 3):
        #     # Skip duplicates for the first element
        #     if i > 0 and nums[i] == nums[i - 1]:
        #         continue

        #     for j in range(i + 1, n - 2):
        #         # Skip duplicates for the second element
        #         if j > i + 1 and nums[j] == nums[j - 1]:
        #             continue

        #         left, right = j + 1, n - 1
        #         while left < right:
        #             current_sum = nums[i] + nums[j] + nums[left] + nums[right]

        #             if current_sum == target:
        #                 result.append([nums[i], nums[j], nums[left], nums[right]])

        #                 # Skip duplicates for the third and fourth elements
        #                 while left < right and nums[left] == nums[left + 1]:
        #                     left += 1
        #                 while left < right and nums[right] == nums[right - 1]:
        #                     right -= 1

        #                 left += 1
        #                 right -= 1
        #             elif current_sum < target:
        #                 left += 1  # Increase the sum by moving the left pointer
        #             else:
        #                 right -= 1  # Decrease the sum by moving the right pointer

        

