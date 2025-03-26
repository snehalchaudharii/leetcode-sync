class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        totalCell= n*n
        maxPossible= maxWeight//w
        return min(maxPossible, totalCell)
            
