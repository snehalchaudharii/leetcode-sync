class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) < 2:
            return False
        
        doubled_string = s + s
        substring_to_check = doubled_string[1:-1]
        return s in substring_to_check
     
