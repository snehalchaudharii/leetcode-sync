class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n= len(grid)
        all_numbers= set(range(1, n*n+1))
        seen= set()
        duplicate= -1
        for row in grid:
            for num in row:
                if num in seen:
                    duplicate= num
                seen.add(num)
        
        missing= list(all_numbers - seen)[0]

        return [duplicate, missing]
        
