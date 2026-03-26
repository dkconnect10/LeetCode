class Solution:
    def isPowerOfThree(self,n,i=0):
        if (3**i)>n:
            return False
            
        if (3**i)==n:
            return True
        return self.isPowerOfThree(n,i+1)