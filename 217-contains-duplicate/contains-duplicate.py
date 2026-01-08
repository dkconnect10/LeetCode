class Solution(object):
    def containsDuplicate(self, nums):
        dict={}
        for num in nums:
            if num in dict:
                return True
            dict[num]=nums
        return False 
        