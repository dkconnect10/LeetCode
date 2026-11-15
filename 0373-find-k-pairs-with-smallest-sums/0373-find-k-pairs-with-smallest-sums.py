class Solution:
    def max_hepify_down(self,heap,i):
        curr = i
        n = len(heap)
        
        while True:
            left = curr*2+1
            right = curr*2+2
            
            if left>=n:
                break
            if right>=n:
                if sum(heap[left])>sum(heap[curr]):
                    heap[left],heap[curr]=heap[curr],heap[left]
                    curr=left
                else:
                    break
            else:
                if sum(heap[left])>sum(heap[right]):
                    if sum(heap[curr])<sum(heap[left]):
                        heap[curr],heap[left]=heap[left],heap[curr]
                        curr=left
                    else:
                        break
                else:
                    if sum(heap[curr])<sum(heap[right]):
                        heap[curr],heap[right]=heap[right],heap[curr]
                        curr=right
                    else:
                        break
                    
    def max_hepify_up(self,heap):
        end = len(heap)-1
        
        while end!=0:
            parent = (end-1)//2
            
            if sum(heap[parent])<sum(heap[end]):
                heap[parent],heap[end]=heap[end],heap[parent]
                end=parent
            else:
                break
            
    
    def kSmallestPairs(self, nums1, nums2, k):
        heap=[]
        
        for i in nums1:
            if len(heap)==k and i+nums2[0] > sum(heap[0]):
                break
            for j in nums2:
                temp= [i,j]
                
                if len(heap)==k:
                    if sum(temp)<sum(heap[0]):
                        heap[0]=temp
                        self.max_hepify_down(heap,0)
                    else:
                        break
                else:
                    heap.append(temp)
                    self.max_hepify_up(heap)       
        return heap  