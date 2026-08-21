class Solution:
    def max_heapfiy_down(self,nums,i):
        n = len(nums)
        curr = i
        while True:
            left = curr*2+1
            right = curr*2+2

            if left>=n:
                break
            if right>=n:
                if nums[curr]<nums[left]:
                    nums[curr],nums[left]=nums[left],nums[curr]
                    curr = left
                else:
                    break
            else:
                if nums[left]>nums[right]:
                    if nums[curr]<nums[left]:
                        nums[curr],nums[left]=nums[left],nums[curr]
                        curr = left
                    else:
                        break
                else:
                    if nums[curr]<nums[right]:
                        nums[curr],nums[right]=nums[right],nums[curr]
                        curr = right
                    else:
                        break

        return nums
    
    def build(self,nums):
        n = len(nums)

        non_leafNode = n//2-1

        for i in range(non_leafNode,-1,-1):
            self.max_heapfiy_down(nums,i)

    def maxProduct(self, nums):
        
        first = None
        second = None

        self.build(nums)

        while first is None or second is None:
            if first is None:
                first=nums[0]
            else:
                second = nums[0]

            nums[0],nums[-1]=nums[-1],nums[0]
            nums.pop()
            self.max_heapfiy_down(nums,0)

        return (first - 1) * (second - 1)  