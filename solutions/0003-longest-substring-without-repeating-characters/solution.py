class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Time Complexity: O(n)
        # Each character is added to longestStr once and removed at most once.
        # Every right move or left move is done in O(1), leading to O(n).
        # Space Complexity: O(min(n, 26))
        # The set stores unique characters, with at most 26 lowercase letters in English.
        # In the worst case, if all characters are unique, the set has n elements.

        count=0
        longstr= set()
        left=0
        right=0
        while right< len(s):
            if s[right] not in longstr:
                longstr.add(s[right])
                count= max(count, right-left+1)
                right+=1
            else:
                longstr.remove(s[left])
                left+=1
        
        return count

            

