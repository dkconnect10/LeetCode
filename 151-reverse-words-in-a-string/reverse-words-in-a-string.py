class Solution:
    def reverseWords(self, s):
        new = (s).split()
        list1=[]
        
        i=len(new)-1
        while i>=0:
            list1.append(new[i])
            i-=1
        return " ".join(list1)