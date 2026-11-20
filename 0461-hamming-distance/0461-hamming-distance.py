class Solution:
    def hammingDistance(self, x, y):
        
        bin1 = bin(x)[2:] 
        bin2 = bin(y)[2:]   
        
        
        max_len = max(len(bin1), len(bin2))
        
       
        bin1_equal = bin1.zfill(max_len)
        bin2_equal = bin2.zfill(max_len)
        
        # print(bin1_equal,bin2_equal)
        
        cnt = 0
        
        i = 0
        while i<len(bin1_equal):
            if bin1_equal[i]!=bin2_equal[i]:
                cnt+=1
            i+=1
        return cnt 