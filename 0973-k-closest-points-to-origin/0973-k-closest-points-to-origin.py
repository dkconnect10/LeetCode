class Solution:
    def heapfiy_down(self,heap,i):
        n=len(heap)
        curr=i
        while True:
            left = curr*2+1
            right = curr*2+2
            
            if left>=n:
                break
            if right>=n:
                if heap[curr][0]<heap[left][0]:
                    heap[curr],heap[left]=heap[left],heap[curr]
                    curr=left
                else:
                    break
            else:
                if heap[left][0]>heap[right][0]:
                    if heap[curr][0]<heap[left][0]:
                        heap[curr],heap[left]=heap[left],heap[curr]
                        curr=left
                    else:
                        break
                else:
                    if heap[curr][0]<heap[right][0]:
                        heap[curr],heap[right]=heap[right],heap[curr]
                        curr=right
                    else:
                        break
        return heap
        
    def insert(self,heap,val):
        heap.append(val)
        
        end = len(heap)-1
        
        while end!=0:
            parent = (end-1)//2
            
            if heap[parent][0]<heap[end][0]:
                heap[parent],heap[end]=heap[end],heap[parent]
                end=parent
            else:
                break
            
    
    def kClosest(self, points, k):
        heap = []
        for point in points:
            x = point[0]
            y = point[1]
            distance = x*x + y*y 

            pair = (distance,point)
            # print("pair:",pair)
            if len(heap)==k:
                if heap[0][0]>pair[0]:
                    heap[0]=pair
                    self.heapfiy_down(heap,0)
                else:
                    continue
            else:
                # print("before insert",heap)
                self.insert(heap,pair)
                # print("after insert",heap)
        # print(heap)    
        
        result = []
        for _,val in heap:
            result.append(val)
        return result