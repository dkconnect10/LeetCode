class Solution(object):
    def removeElement(self, nums, val):
        low = 0
        for mid in range(len(nums)):
            if nums[mid]!=val:
                nums[mid],nums[low]=nums[low],nums[mid]
                low+=1
        return low