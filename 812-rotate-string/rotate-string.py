class Solution:
    def rotateString(self,s,goal):
         i=0
         x=list(s)
         while i<len(x):
             x.append(x[0])
             x.pop(0)  
             if ''.join(x)==goal:
                 return True
             i+=1
         return False   