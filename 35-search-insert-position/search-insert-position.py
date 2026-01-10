class Solution(object):
    def searchInsert(self, nums, target):
        low = 0
        high = len(nums)-1
        ans =len(nums)
 
        while low<=high:
            mid = (low+high)//2
            if nums[mid]>=target:
                ans = mid
                high = mid-1
            else:
                low=mid+1
        return ans    