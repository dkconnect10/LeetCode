# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self,lists):
        freq = []
        cnt=1
        for node in lists:
            temp = node
            while temp:
                freq.append(temp.val)
                temp = temp.next
            cnt+=1 
            
        freq.sort()
        
        heap = None
        
        for i in freq:
            if not heap:
                heap = ListNode(i)
            else:
                temp = heap
                while temp.next:
                    temp = temp.next
                temp.next = ListNode(i)
            
        return heap
        