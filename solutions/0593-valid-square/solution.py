class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def distance(p1, p2):
            return (p1[0]-p2[0]) ** 2 + (p1[1]-p2[1]) ** 2

        points= [tuple(p1), tuple(p2), tuple(p3), tuple(p4)]
        if len(set(points))!=4:
            return False
        
        distances=[]
        for i in range(4):
            for j in range(i+1, 4):
                distances.append(distance(points[i], points[j]))
        distances.sort()

        return (len(distances)==6 and
                distances[0]==distances[1]==distances[2]==distances[3] and
                distances[4]==distances[5] and
                distances[0]>0 and
                distances[4] == 2* distances[0])
        
# TC SC: O(1)
