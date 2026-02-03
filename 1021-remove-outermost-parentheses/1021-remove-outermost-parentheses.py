class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        temp=[]
        opend=0
        for i in s:
            if i=="(" and opend>0:temp.append(i)
            if i==")" and opend>1:temp.append(i)
            opend+=1 if i=="(" else -1
        return "".join(temp)   
        