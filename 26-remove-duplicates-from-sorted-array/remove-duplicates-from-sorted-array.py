class Solution(object):
    def removeDuplicates(self, nums):
        value = []
        for i in nums:
            if i not in value:
                value.append(i)
        for i,val in enumerate(value):
            nums[i]=val
            
        return len(value)