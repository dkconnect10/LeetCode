class Solution(object):
    def maxSubArray(self, nums):
        max_sum = float('-inf')
        curr_sum = 0
        
        for num in nums:
            curr_sum += num
            if curr_sum > max_sum:
                max_sum = curr_sum
            if curr_sum < 0:
                curr_sum = 0
                
        return max_sum
