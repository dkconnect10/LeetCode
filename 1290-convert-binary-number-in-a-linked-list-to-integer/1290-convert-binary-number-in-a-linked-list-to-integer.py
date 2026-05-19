# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseLinkLIst(self,head):
        temp=head
        prev = None
        while temp:
            front = temp.next
            temp.next=prev
            prev=temp
            temp=front
        head=prev
        return head

    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        head = self.reverseLinkLIst(head)
        temp = head
        num = 0
        p = 1
        while temp:
            if temp.val==1:
                num+=p
            p=p*2
            temp=temp.next
        return num        
    