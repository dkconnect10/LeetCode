class Solution:
    def multiply(self, num1, num2):
        if len(num2)<len(num1):
            num1,num2=num2,num1
            
        i=len(num1)-1
        sum=0
        rem="0"
        freq=""

        while i>-1:
            j=len(num2)-1
            while j>-1:
                prod = str(int(num1[i])*int(num2[j]))
                # print(int(num1[i])*int(num2[j]))
                # print("**:",prod)
                # print("**:",rem)
                if len(rem)>0:
                    prod=str(int(prod)+int(rem))
                # print("after add rem:",prod)
                # print("available rem:",rem)
                rem=""
                if len(prod)>1 and j!=0:
                    freq+=prod[-1]
                    rem=prod[:-1]
                    # print("new rem:",rem)
                else:
                    freq+=prod[::-1]
                j-=1
                # print("sum:",sum,"rem:",rem,"freq:",freq)
                # input()
            freq =("0" * (len(num1)-1-i))+freq    
            sum+=int(freq[::-1])
            freq=""
            rem="0"
            i-=1
        return str(sum)