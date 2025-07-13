class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_val= {val: idx for idx, val in enumerate((list1))}
        
        result= []
        min_val= float("inf")

        for j, val in enumerate((list2)):
            if val in index_val:
                i= index_val[val]
                total = i+j
                if total < min_val:
                    min_val = total
                    result= [val]
                elif total == min_val:
                    result.append(val)
        return result
            

