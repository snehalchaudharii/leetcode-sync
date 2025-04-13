class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row= len(matrix)
        col= len(matrix[0])
        r=0
        c= col-1
        while (r< row and c >=0):
            if target == matrix[r][c]:
                return True
            elif target < matrix[r][c]:
                c=c-1
            else:
                r=r+1
        return False
