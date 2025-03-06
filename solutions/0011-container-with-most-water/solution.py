class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Brute force apporoach gives time limit exceeded error
        # maxWater= 0
        # for i in range(len(height)):
        #     for j in range(i+1, len(height)):
        #         width = j-i
        #         h= min(height[i], height[j])
        #         area= width * h
        #         maxWater= max(area, maxWater)
        # return maxWater

        maxWater=0
        left=0
        right= len(height)-1
        while left<right:
            width= right-left
            h= min(height[left],height[right])
            area= width * h
            maxWater = max(maxWater, area)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxWater






        # left=0
        # right=len(height)-1
        # maxArea=0

        # while left<right:
        #     currentArea = min(height[left], height[right]) * (right - left)
         
        #     maxArea= max(maxArea, currentArea)

        #     if height[left]<height[right]:
        #         left+=1
        #     else:
        #         right-=1
        # return maxArea

