class Solution:
    def is_prime(self,n):
        if n <= 1: return False 
        for i in range(2, int(n**0.5) + 1): 
            if n % i == 0:
                return False 
        return True 
        
    def countPrimeSetBits(self, left, right):
        cnt = 0
        for i in range(left,right+1):
            val = bin(i)[2:].count("1")
            if self.is_prime(val):
                cnt+=1
        return cnt