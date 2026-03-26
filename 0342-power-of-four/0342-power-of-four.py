class Solution:
    def isPowerOfFour(self,n,i=0):
        if (4**i)>n:
            return False
            
        if (4**i)==n:
            return True
        return self.isPowerOfFour(n,i+1)