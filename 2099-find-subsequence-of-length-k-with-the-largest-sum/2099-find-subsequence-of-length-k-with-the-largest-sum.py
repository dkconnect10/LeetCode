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
                if nums[curr][0]>nums[left][0]:
                    nums[curr],nums[left]=nums[left],nums[curr]
                    curr=left
                else:
                    break
            else:
                if nums[left][0]<nums[right][0]:
                    if nums[curr][0]>nums[left][0]:
                        nums[curr],nums[left]=nums[left],nums[curr]
                        curr=left
                    else:
                        break
                else:
                    if nums[curr][0]>nums[right][0]:
                        nums[curr],nums[right]=nums[right],nums[curr]
                        curr=right
                    else:
                        break    
        return nums

    def heapify_up(self,nums):
        n = len(nums)
        end = n-1

        while end!=0:
            parent =(end-1)//2
            if nums[parent][0]>nums[end][0]:
                nums[parent],nums[end]=nums[end],nums[parent]
                end=parent
            else:
                break

    def build(self,nums):
        n = len(nums)
        non_leafnode = n//2-1

        for i in range(non_leafnode,-1,-1):
            self.heapify_down(nums,i)

    def maxSubsequence(self, nums, k):
        temp = []
        heap = []
        
        for i in range(len(nums)):
            temp.append((nums[i],i))
        print(temp)
        
        for i in temp:
            if len(heap)==k:
                if heap[0][0]<i[0]:
                    heap[0]=i
                    self.heapify_down(heap,0)
                else:
                    continue    
            else:
                heap.append(i)  
                self.heapify_up(heap)  

        heap.sort(key = lambda x: x[1])
        return [x[0] for x in heap]  