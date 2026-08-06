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
    def insert(self,heap,value):
        heap.append(value)
        n = len(heap)
        current = n-1
        while current!=0:
            parent=(current-1)//2
            if heap[parent][0]>heap[current][0]:
                heap[parent],heap[current]=heap[current],heap[parent]
                current=parent
            else:
                break
            
        return heap
        
    def topKFrequent(self, nums, k):
        freq = {}
        for i in nums:
            freq[i]=freq.get(i,0)+1
            
            

        heap =[]
        
        for key,val in freq.items():
            pair = (val,key)
                
            if len(heap)==k:
                if heap[0][0]<pair[0]:
                    heap[0]=pair
                    heap = self.min_heapfiy_down(heap,0)
                else:
                    continue
            else:
                heap = self.insert(heap,pair)
        result = []        
        for _,value in heap:
            result.append(value)
        return result 