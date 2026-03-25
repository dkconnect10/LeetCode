class Solution:
    def marge(self,nums,low,mid,high):
        temp=[]
        first=low
        second=mid+1
        
        while first<=mid and second<=high:
            if nums[first]<=nums[second]:
                temp.append(nums[first])
                first+=1
            else:
                temp.append(nums[second])
                second+=1
                
        while first<=mid:
            temp.append(nums[first])
            first+=1
        while second<=high:
            temp.append(nums[second])
            second+=1
            
        nums[low:high+1]=temp    
        return nums
        
    def sortArray(self, nums,low=0,high=None):
        if len(nums)<2:
            return nums
        if high is None:
            high=len(nums)-1
        if low>=high:
            return
        mid = (low+high)//2
        self.sortArray(nums,low,mid)
        self.sortArray(nums,mid+1,high)
        self.marge(nums,low,mid,high)
        return nums