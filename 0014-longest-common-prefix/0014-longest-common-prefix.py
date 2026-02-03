class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs)==1:
            return strs[0]
        start=strs[0]
 
        for i in range(len(start)):
            for j in range(1,len(strs)):
                if i >=len(strs[j])  or start[i]!=strs[j][i]:
                    return start[:i]
        return start  