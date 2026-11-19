class Solution:
    def evenOddBit(self, n):
        binary = bin(n)[2:]
        print(binary)
        
        even=0
        odd=0
        
        i=len(binary)-1
        
        while i>=0:
            question_index=len(binary)-1-i
            if question_index%2==0:
                # print("index:",i,binary[i])
                if binary[i]=="1":
                    even+=1
            else:
                if binary[i]=="1":
                    odd+=1
            i-=1
        
        return [even,odd] 