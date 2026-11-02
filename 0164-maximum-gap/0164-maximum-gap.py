class Solution:
    def maximumGap(self, nums):
        n = len(nums)
        
        maxGap = 0
        
        nums.sort()
        
        if n<2:
            return 0
            
        for i in range(n-1):
            maxGap = max(maxGap , nums[i+1]-nums[i])
            
        return maxGap