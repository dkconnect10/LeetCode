class Solution:
    def heapify_down(self,nums,i):
        n = len(nums)
        curr = i

        while True:
            left = curr*2+1
            right = curr*2+2

            if left>=n:
                break
            if right>=n:
                if nums[curr]>nums[left]:
                    nums[curr],nums[left]=nums[left],nums[curr]
                    curr=left
                else:
                    break
            else:
                if nums[left]<nums[right]:
                    if nums[curr]>nums[left]:
                        nums[curr],nums[left]=nums[left],nums[curr]
                        curr=left
                    else:
                        break
                else:
                    if nums[curr]>nums[right]:
                        nums[curr],nums[right]=nums[right],nums[curr]
                        curr=right
                    else:
                        break    
        return nums
        
    def delete(self,nums):
        nums[0],nums[-1]=nums[-1],nums[0]
        nums.pop()
        self.heapify_down(nums,0)
        return nums

    def build(self,nums):
        n = len(nums)
        end = n-1
        nonleaf_node = n//2-1
        for i in range(nonleaf_node,-1,-1):
            self.heapify_down(nums,i)
        return nums

    def numberGame(self, nums):
        arr = []

        self.build(nums)
        while nums:
            alice = nums[0]
            self.delete(nums)
            bob = nums[0]
            self.delete(nums)
            arr.append(bob)
            arr.append(alice)
        return arr  