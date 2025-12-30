class Solution(object):
    def sortArrayByParity(self, nums):
        n = len(nums)
        low = 0
        mid = 0
        high = n-1
        
        while mid<= high:
            if nums[mid]%2==0:
                nums[low],nums[mid]=nums[mid],nums[low]
                mid+=1
                low+=1
            else:
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1
        return nums       
                
        