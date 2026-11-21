class Solution:
    def hasAlternatingBits(self, n):
        val = bin(n)[2:]

        if len(val)<2:
            return True
            
        i=0
        
        while i<len(val)-1:
            if val[i]==val[i+1]:
                return False
            i+=1
        return True