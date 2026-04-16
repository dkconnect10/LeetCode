class Solution:
    def wordPattern(self, pattern, s):
        new = s.split(" ")
        dict={}
        dict1={}
        i=0
        
        if len(pattern) != len(new):
            return False
        
        while i<len(pattern):
            if (dict.get(pattern[i]) and dict.get(pattern[i])!=new[i]) or \
               (dict1.get(new[i]) and dict1[new[i]]!=pattern[i]):
                return False
            else:    
                dict[pattern[i]]=new[i]
                dict1[new[i]]=pattern[i]
            i+=1
        return True