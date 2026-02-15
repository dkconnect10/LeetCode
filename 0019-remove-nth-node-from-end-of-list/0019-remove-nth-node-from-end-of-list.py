# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self,head, n):  
        if not head:
            return None

        temp = head
        prev = None
        
        while temp is not None:
            front = temp.next
            temp.next=prev
            prev=temp
            temp=front
        head=prev
        
        if n==1:
            head=head.next
        else:
            temp=head
            count = 1

            while temp and count < n-1:
                temp=temp.next
                count+=1

            if temp and temp.next:
                temp.next = temp.next.next        
        
        temp=head
        prev = None
        while temp is not None:
            front = temp.next
            temp.next=prev
            prev=temp
            temp=front
        head=prev
        return head
    