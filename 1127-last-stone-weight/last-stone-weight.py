class Solution:
    def heapify_down(self,heap,i):
        curr = i
        n=len(heap)
        while True:
            left = curr*2+1
            right = curr*2+2
            if left>=n:
                break
            if right>=n:
                if heap[curr]<heap[left]:
                    heap[curr],heap[left]=heap[left],heap[curr]
                    curr=left
                else:
                    break
            else:
                if heap[left]>heap[right]:
                    if heap[curr]<heap[left]:
                        heap[curr],heap[left]=heap[left],heap[curr]
                        curr=left
                    else:
                        break
                else:
                    if heap[curr]<heap[right]:
                        heap[curr],heap[right]=heap[right],heap[curr]
                        curr=right
                    else:
                        break
        return heap
        
    def delete(self,heap):
        heap[0],heap[-1]=heap[-1],heap[0]
        heap.pop(-1)
        if heap:
            heap =self.heapify_down(heap,0)
        return heap
   
    def insert(self,stones, val):
        stones.append(val)
        n=len(stones)
        # print("n",n)
        
        end=n-1
        
        while end!=0:
            parent=(end-1)//2
            # print("parent:",parent)
            if stones[parent]<stones[end]:
                stones[parent],stones[end]=stones[end],stones[parent]
                end=parent
            else:
                break
        return stones    

    def build(self,heap):
        n = len(heap)-1
        parent = (n-1)//2
        for i in range(parent,-1,-1):
            heap =self.heapify_down(heap,i)
        return heap    
        
    def lastStoneWeight(self, stones):
        stones = self.build(stones)
        while len(stones)>1:
            # print("starting Stongs ::::::::::::::::::::",stones)
            first = stones[0]
            stones = self.delete(stones)
            
            second = stones[0]
            stones = self.delete(stones)
            
            if first != second:
                
                val = first-second
                # print("first,second,val",first,second,val,stones)
                self.insert(stones,val)
                # print("after insert stones",stones)
            else:
                # print("stones of equla *****************",stones)
                continue
               
        if stones:
            return stones[0]
        return 0