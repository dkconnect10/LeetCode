# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        temp=head
        num=0
        while temp:
            num = num*2+temp.val
            temp=temp.next
        return num    
        