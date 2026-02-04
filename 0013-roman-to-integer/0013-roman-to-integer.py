class Solution:

    def romanToInt(self, s: str) -> int:

        temp=[]

        temp1=[]

        for i in s:

            if i=="I":temp.append(1)

            if i=="V":temp.append(5)

            if i=="X":temp.append(10)

            if i=="L":temp.append(50)

            if i=="C":temp.append(100)

            if i=="D":temp.append(500)

            if i=="M":temp.append(1000)

        if len(temp)==1:

            return temp[0]

        if len(temp)==0:

            return ""

        j=len(temp)-1

        while j>0:

            if temp[j-1]<temp[j]:

                temp1.append(temp[j]-temp[j-1])

                j-=1

            else:    

                temp1.append(temp[j])

            j-=1

        print(temp)    

        if temp[0]>=temp[1]:

            temp1.append(temp[0])

        return sum(temp1)
 