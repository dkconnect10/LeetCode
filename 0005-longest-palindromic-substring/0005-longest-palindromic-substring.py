class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        
        for i in range(len(s)):
            a = expand(i, i)
            b = expand(i, i+1)
            
            if len(a) > len(res):
                res = a
            if len(b) > len(res):
                res = b
        
        return res