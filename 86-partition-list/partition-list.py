class Solution:    
    def partition(self,head, x):
            if head is None:
                return head
            gll=None
            sll=None
            temp=head
            
            while temp:
                if temp.val>=x:
                    n = ListNode(temp.val,gll)
                    gll=n
                else:
                    n=ListNode(temp.val,sll)
                    sll=n
                temp=temp.next
            
            temp = gll
            prev=None
            while temp:
                front=temp.next
                temp.next=prev
                prev=temp
                temp=front
            rev_gll=prev

            temp = sll
            prev=None
            while temp:
                front=temp.next
                temp.next=prev
                prev=temp
                temp=front 
            rev_sll=prev    
                
            temp=head
            if rev_sll:
                while temp:
                    temp.val=rev_sll.val
                    if rev_sll.next:
                        rev_sll=rev_sll.next
                        temp=temp.next
                    else:
                        break
            if rev_gll:    
                if not rev_sll:
                    temp=head
                elif temp.next:
                    temp=temp.next
                    
                    while temp:
                        temp.val=rev_gll.val
                        if rev_gll.next:
                            rev_gll=rev_gll.next
                            temp=temp.next
                        else:
                            break
            return head