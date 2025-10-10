class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n):
            for j in range(i,n-1):
                if nums[i] + nums[j+1] == target:
                    return  i , j+1
              
nums = [2,7,11,15]        
target = 9
obj = Solution()
print(obj.twoSum(nums,target))

 