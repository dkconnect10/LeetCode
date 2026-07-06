class Solution:
    def maxVowels(self, s, k):
        vowels = {"a","e","i","o","u"}
        vmax = 0
        count = 0
        for i in range(len(s)):
            if s[i] in vowels:
                count+=1
            if i>=k:
                if s[i-k] in vowels:
                    count-=1
            if i>= k-1:
                vmax = max(count,vmax)    
        return vmax 