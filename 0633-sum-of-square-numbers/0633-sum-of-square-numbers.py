class Solution:
    def judgeSquareSum(self, c):
        i=0
        j=int(c**0.5)
        
        while i<=j:
            curr = (i*i)+(j*j)
            if curr==c:
                return True
            elif curr<c:
                i+=1
            else:
                j-=1
        return False 
 