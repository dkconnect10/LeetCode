class Solution:
    def isPowerOfTwo(self, n):
        i=0
        while 2**i<=n:
            if (2**i)==n:
                return True
            i+=1    
        return False 