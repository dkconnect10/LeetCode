class Solution(object):
    def maxSubArray(self, nums):
        n = len(nums)
        max_len =float('-inf')
        count=0
        
        for i in range(0,n):
            count+=nums[i]
    
            if count>max_len:
                max_len = max(max_len,count)
            
            if count<0:
                count=0    
                
        return max_len 