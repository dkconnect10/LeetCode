class Solution(object):
    def removeElement(self, nums, val):
        nums [:] =[f for f in nums if f != val]
        return len(nums)
        