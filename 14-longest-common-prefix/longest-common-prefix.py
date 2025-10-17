class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        first_str = strs[0]
        
        for i in range(len(first_str)):
            char = first_str[i] 
            for j in range(1,len(strs)):
                if i >= len(strs[j]) or strs[j][i] != char:
                    return first_str[:i] 
        return first_str