import math 

class Solution:
    def heapify_down(self,nums,i):
        n=len(nums)
        current = i
        while True:
            left=current*2+1
            right=current*2+2
            if left>n-1:
                break
            if right>n-1:
                if nums[current]<nums[left]:
                    nums[current],nums[left]=nums[left],nums[current]
                    current=left
                else:
                    break
            else:
                if nums[left]>nums[right]:
                    if nums[current]<nums[left]:
                        nums[current],nums[left]=nums[left],nums[current]
                        current=left
                    else:
                        break
                else:
                    if nums[current]<nums[right]:
                        nums[current],nums[right]=nums[right],nums[current]
                        current=right
                    else:
                        break
        return nums

    def build(self,nums):
        n = len(nums)
        if n==0:
            return nums
        parent = n//2-1
        for i in range(parent,-1,-1):
            self.heapify_down(nums,i)

    def pickGifts(self, gifts, k):
        
        self.build(gifts)
        
        while k:
            gifts[0] = math.isqrt(gifts[0])
            self.heapify_down(gifts,0)
            k-=1
        return sum(gifts)