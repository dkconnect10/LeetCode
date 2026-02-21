class Solution:
    def __init__(self):
        self.head = None
        
    def addTwoNumbers(self,l1,l2):
        
        temp_list1= []
        
        temp=l1
        while temp:
            temp_list1.append(temp.val)
            temp=temp.next
            
        val = [str(i) for i in reversed(temp_list1)]
        new = ''.join(val)
        
        
        temp_list2= []
        
        temp=l2
        while temp:
            temp_list2.append(temp.val)
            temp=temp.next
            
        val2 = [str(i) for i in reversed(temp_list2)]
        new2 = ''.join(val2)
        new3 = int(new2)+int(new)
        
        
        head = None
        
        for i in str(new3):
            n = ListNode(int(i))
            n.next=head
            head=n
        
        
        return head