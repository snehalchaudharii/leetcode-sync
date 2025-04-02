class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs)==1:
            return strs[0]
        
        min_length= min(len(s) for s in strs)

        for i in range(min_length):
            char= strs[0][i]
            for string in strs[1:]:
                if string[i]!= char:
                    return strs[0][:i]
        return strs[0][:min_length]
