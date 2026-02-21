# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1,list2):
        temp=[]
        first=list1
        second = list2
        
        while first and second:
            if first.val<=second.val:
                temp.append(first.val)
                first=first.next
            else:
                temp.append(second.val)
                second=second.next
        while first:
            temp.append(first.val)
            first=first.next
        while second:
            temp.append(second.val)
            second=second.next
        
        head = None
        for i in reversed(temp):
            n = ListNode(i,head)
            head=n
        return head