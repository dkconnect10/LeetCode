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
                if nums[curr]<nums[left]:
                    nums[curr],nums[left]=nums[left],nums[curr]
                    curr=left
                else:
                    break
            else:
                if nums[left]>nums[right]:
                    if nums[curr]<nums[left]:
                        nums[curr],nums[left]=nums[left],nums[curr]
                        curr=left
                    else:
                        break
                else:
                    if nums[curr]<nums[right]:
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

    def deleteGreatestValue(self, grid):        
        result = 0

        while True:
            # print("grid",grid)
            heap = []

            for i in grid:
                temp = self.build(i)
                # print("temp",temp)
                heap.append(temp[0])
                # print("after append heap : ",heap)
                self.delete(temp)
                # print("after delete grid",i)

                    
            if len(heap)>0:        
                self.build(heap)
                result+=heap[0]
                # print("result:",result)
            if all(len(arr)==0 for arr in grid):
                break 
        # print("result:",result)
        return result