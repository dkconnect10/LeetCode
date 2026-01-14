class Solution:
    def search(self, nums, k):
        low=0
        high=len(nums)-1
        
        while low<=high:
            mid=(low+high)//2
            
            if nums[mid]==k:
                return mid
            if nums[low]<=nums[mid]:
                if nums[low]<=k and k<=nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            else:
                if nums[mid]<=k and nums[high]>=k:
                    low=mid+1
                else:
                    high=mid-1
        return -1 
        