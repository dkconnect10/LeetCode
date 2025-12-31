class Solution:
    def maxAbsoluteSum(self, nums):
        min_len=0
        max_len = 0
        
        count_pos=0
        count_nag=0
        
        for i in nums:
            count_pos+=i
            
            if count_pos>max_len:
                max_len = count_pos
            
            if count_pos < 0:
                count_pos = 0
            
            count_nag+=i
            
            if count_nag<min_len:
                min_len=count_nag
                
            if count_nag > 0:
                count_nag = 0
        return max(abs(max_len),abs(min_len))