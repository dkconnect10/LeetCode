class Solution:
    def removeDuplicates(self, nums):
        temp = []
        for i in range(len(nums)):
            if nums[i] not in temp:
                temp.append(nums[i])
        nums[:]=temp
        return len(nums)