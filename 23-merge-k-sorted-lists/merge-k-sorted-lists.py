# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def heapfiy_down(self,nums,i):
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
        
    def build(self,nums):
        n = len(nums)
        none_leafnode  = n//2-1
        
        for i in range(none_leafnode,-1,-1):
            self.heapfiy_down(nums,i)
        return nums
        
    def mergeKLists(self, lists):
        heap=[]

        for nodes in lists:
            if nodes:
                heap.append((nodes.val,nodes))
            
        self.build(heap)
        
        front = None
        current = None
        
        while heap:
            
            value = heap[0][0]
            original_node = heap[0][1]
            
            node = ListNode(value)
            
            if front     is None:
                front=node
                current=node
            else:
                current.next=node
                current=node
            
            next_node = original_node.next 
            
            if next_node:
                heap[0] = (next_node.val,next_node)
                self.heapfiy_down(heap,0)
            else:
                heap[0],heap[-1]=heap[-1],heap[0]
                heap.pop()
                
                if heap:
                    self.heapfiy_down(heap, 0)    
        return front    
    
        