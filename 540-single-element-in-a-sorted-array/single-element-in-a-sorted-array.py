class Solution:
    def singleNonDuplicate(self, nums):
        dict1 = {}
        for num in nums:
           dict1[num]=dict1.get(num,0)+1
        
        for key,value in dict1.items():
            if value==1:
                return key