class Solution:
    def lengthOfLongestSubstring(self, s):
        if len(s)<2:
            return len(s)
        temp = ""
        max=0
        
        i=0
        while i<len(s):
            # print("i***:",s[i])
            j=i
            while j<len(s):
                # print("j:",s[j])
                if s[j] in temp:
                    if len(temp)>max:
                        max=len(temp)
                    temp=""
                    break
                else:
                    temp+=s[j]
                    j+=1
            i+=1    
        return max