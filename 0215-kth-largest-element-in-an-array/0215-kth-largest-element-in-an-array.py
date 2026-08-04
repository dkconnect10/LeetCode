class Solution:
    def min_heapfiy_down(self,nums,i):
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
    
    def insert(self,heap,value):
        heap.append(value)
        n = len(heap)
        current = n-1
        while current!=0:
            parent=(current-1)//2
            if heap[parent]>heap[current]:
                heap[parent],heap[current]=heap[current],heap[parent]
                current=parent
            else:
                break
            
        return heap    
            
    def findKthLargest(self, nums, k):
        n = len(nums)
        heap =[]
        
        for i in range(n):
            if len(heap)>=k:
                if heap[0]<nums[i]:
                    heap[0]=nums[i]
                    heap = self.min_heapfiy_down(heap,0)
                else:
                    continue
            else:
                heap = self.insert(heap,nums[i])
        return heap[0]           