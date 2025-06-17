class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        
        if len(strs)==1:
            return strs[0]

        min_length= min(len(s) for s in strs)

        for i in range(min_length):
            char = strs[0][i]
            for string in strs[1:]:
                if string[i]!=char:
                    return strs[0][:i]

        # All characters matched up to min_length
        return strs[0][:min_length]

# Time Complexity: O(S), where S is the sum of characters in the common prefix across all strings.
# Worst case: O(n * m), where n = len(strs), m = min string length.
# Space Complexity: O(1)
# Only uses a few variables, no extra data structures.
