class Solution:
    def isSorted(self,nums):
        # print("isSorted",nums)
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                return False
        # print("True")            
        return True            
    def minimumPairRemoval(self, nums):
        count=0
        while not self.isSorted(nums):
            freq ={}
            for i in range(len(nums)-1):
                freq[i]=nums[i]+nums[i+1]
                
            # print(freq)    
            minv=float("inf")
            index = None
            for key,value in freq.items():
                if value<minv:
                    minv=value
                    index=key
            nums[index+1]=minv
            count+=1
            nums.pop(index)
            # print(nums)
            freq={}
        return count