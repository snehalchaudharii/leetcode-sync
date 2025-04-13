class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows= len(matrix)
        cols= len(matrix[0])
        srow=0
        erow= rows-1
        scol=0
        ecol= cols-1
        ans=[]
        while(srow<=erow and scol<=ecol):

            for j in range(scol, ecol+1):
                ans.append(matrix[srow][j])
            srow+=1
            for i in range(srow, erow+1):
                ans.append(matrix[i][ecol])
            ecol-=1

            if srow <= erow:
                for j in range(ecol, scol-1, -1):
                    ans.append(matrix[erow][j])
                erow-=1
            
            if scol <= ecol:
                for i in range(erow, srow-1, -1):
                    ans.append(matrix[i][scol])
                scol+=1
        return ans  
           
            
            
            

        

