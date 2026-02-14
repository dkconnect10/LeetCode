# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self,head):
        slow=head
        fast=head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            
        prev = None
        if fast!=None:
            slow=slow.next
            
        while slow is not None:
            front = slow.next
            slow.next=prev
            prev=slow
            slow=front
        
        first=head
        second=prev
        while second is not None:
            if first.val!=second.val:
                return False
            first = first.next
            second = second.next
        return True 

        