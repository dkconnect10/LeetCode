class Solution(object):
    def intersection(self, nums1, nums2):
        dict1 = {}
        dict2 = {}
        list1=[]
        
        for num in nums1:
            if num not in dict1:
                dict1[num]=num
        for num in nums2:
            if num not in dict2:
                dict2[num]=num
        for key,_ in dict1.items():
            if key in dict2:
                list1.append(key)
        return list1