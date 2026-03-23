class Solution:
    def largestNumber(self, nums):
        result = ""
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i==j:
                    continue
                else:
                    first=str(nums[i])
                    second=str(nums[j])
                    if (first+second)>(second+first):
                        nums[i], nums[j] = nums[j], nums[i]
        # print(nums)   
        if nums[0]==0:
                return "0"
        for i in nums:
            result+=str(i)
        return result 