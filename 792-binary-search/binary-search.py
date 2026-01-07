class Solution(object):
    def search(self, nums, target):
        i=0
        while i<len(nums):
            if nums[i]==target:
                return i
            i+=1
        return -1
        
        