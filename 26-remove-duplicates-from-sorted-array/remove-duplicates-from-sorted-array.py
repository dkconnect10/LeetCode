class Solution(object):
    def removeDuplicates(self, nums):
        flist = []
        for i in range(len(nums)):
            if nums[i] not in flist:
                flist.append(nums[i])
                
        nums[:]=flist
        return len(nums)