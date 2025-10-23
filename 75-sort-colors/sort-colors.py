class Solution(object):
    def sortColors(self, nums):
        for i in range(len(nums)):
            for j in range(0,len(nums)-i-1):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        return nums
        