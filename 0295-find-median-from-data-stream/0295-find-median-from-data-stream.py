class MedianFinder:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []
    
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
    
    def min_heapify_up(self,nums):
        n = len(nums)
        end = n-1
        while end!=0:
            parent = (end-1)//2
            if nums[parent]>nums[end]:
                nums[parent],nums[end]=nums[end],nums[parent]
                end=parent
            else:
                break
        return nums    
    
    def max_heapify_up(self,nums):
        n = len(nums)
        end = n-1
        while end!=0:
            parent = (end-1)//2
            if nums[parent]<nums[end]:
                nums[parent],nums[end]=nums[end],nums[parent]
                end=parent
            else:
                break
        return nums
    
    def addNum(self, num):
        if len(self.max_heap)==0:
            self.max_heap.append(num)
        elif self.max_heap[0]<=num:
            self.min_heap.append(num)
            self.min_heapify_up(self.min_heap)
        else:
            self.max_heap.append(num)
            self.max_heapify_up(self.max_heap)
            
        min_len= len(self.min_heap)
        max_len = len(self.max_heap)
        
        if max_len-min_len==2:
            self.max_heap[0],self.max_heap[-1]=self.max_heap[-1],self.max_heap[0]
            value = self.max_heap.pop()
            self.max_heapfiy_down(self.max_heap,0)
            self.min_heap.append(value)
            self.min_heapify_up(self.min_heap)
        elif min_len-max_len==2:
            self.min_heap[0],self.min_heap[-1]=self.min_heap[-1],self.min_heap[0]
            value = self.min_heap.pop()
            self.min_heapfiy_down(self.min_heap,0)
            self.max_heap.append(value)
            self.max_heapify_up(self.max_heap)
        else:
            pass
        
        # print("min_heap",self.min_heap)
        # print("max_heap",self.max_heap)

    def findMedian(self):
        if len(self.min_heap)==len(self.max_heap):
            mid = (self.min_heap[0]+self.max_heap[0])/2
            return mid
        else:
            if len(self.min_heap)>len(self.max_heap):
                return self.min_heap[0]
            else:
                return self.max_heap[0]

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()