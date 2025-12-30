class Solution(object):
    def moveZeroes(self, nums):
        low = 0
        for mid in range(len(nums)):
            if nums[mid]!=0:
                nums[mid],nums[low]=nums[low],nums[mid]
                low+=1
        return nums
        