class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # search space idx start=0 and idex end= n-1 does not exist coz it is not peak point

        # to be a peak point, point should be greater than previous and next value i.e arr[n-1]<arr[n]>arr[n+1]

        start= 1
        end= len(arr)-2

        while(start<= end):
            mid= start+(end-start)//2
            if arr[mid-1]<arr[mid]>arr[mid+1]:
                return mid
            
            # To check if mid point is on the increasing side or decreasing side if it is on increasing side then need to search in right side and if it is in deceresing side then need to check mid in left side

            elif arr[mid-1]<arr[mid]:
                start= mid+1
            else:
                end= mid-1
        return -1
