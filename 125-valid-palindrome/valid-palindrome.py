class Solution(object):
    def isPalindrome(self, s):
        clean = []
        for i in s:
            if i.isalnum():
                clean.append(i.lower())
        def check(clean,start,end):
            if start>=end:
                return True
            if clean[start] != clean[end]:
                return False
            return check(clean,start+1,end-1)    
        return check(clean,0,len(clean)-1) 

        