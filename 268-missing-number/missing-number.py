class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        actual_sum = n*(n+1)//2
        get_sum = sum(nums)
        return actual_sum-get_sum
        