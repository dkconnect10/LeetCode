class Solution:
    def isPowerOfTwo(self,n,i=0):
        if (2**i)>n:
            return False
            
        if (2**i)==n:
            return True
        return self.isPowerOfTwo(n,i+1) 