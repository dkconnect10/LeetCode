class Solution:
    def countGoodSubstrings(self, s):
        if len(s) < 3:
            return 0
        k = 3
        count=0
        temp = list(s[:3])
        if len(set(temp))==k:
                count+=1
        for i in range(k,len(s)):
            temp.pop(0)
            temp.append(s[i])
            if len(set(temp))==k:
                count+=1
        return count 