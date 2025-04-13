class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row= len(matrix)
        col= len(matrix[0])
        # Binary serach on total number of rows
        start= 0
        end= row-1
        while start<=end:
            mid= start + (end- start)//2
            if target>= matrix[mid][0] and target <= matrix[mid][col-1]:
                # found the row => binary search on specific row
                return self.searchInRow(matrix, target, mid)
            elif target >= matrix[mid][col-1]:
                start= mid+1
            else:
                end= mid-1
        return False

    def searchInRow(self, matrix, target, row):
        col= len(matrix[0])

        start=0
        end= col-1

        while start<= end:
            mid= start + (end-start)//2
            if target == matrix[row][mid]:
                return True
            elif target > matrix[row][mid]:
                start= mid+1
            else:
                end= mid-1
        return False

        # TC (O^2)
        # for i in range(row):
        #     for j in range(col):
        #         if matrix[i][j]==target:
        #             return True
        # return False
