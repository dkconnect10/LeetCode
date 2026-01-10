class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict:
                if abs(dict[nums[i]]-i)<= k:
                    return True
            dict[nums[i]]=i
        return False 
        