import math

class Solution:
    def intToRoman(self, num):
        space = []
        result = ""
        roman = {"1000":"M","500":"D","100":"C","50":"L","10":"X","5":"V","1":"I"}
        print(roman)
        while num>0:
            module=0
            if len(str(num))==4:
                module=1000
            elif len(str(num))==3:
                module=100
            elif len(str(num))==2:
                module=10
            else:
                module=1
 
            val = (math.floor(num/module))*module
            space.append(val)
            num =num-val
        print(space)
        
        for i in space:
            if i in roman and int(str(i)[0])!=4 and int(str(i)[0])!=9:
                result+=roman[str(i)]
            elif not i in roman and int(str(i)[0])!=4 and int(str(i)[0])!=9:
                while i>0:
                    for key,value in roman.items():
                        if int(key)<=i:
                            result+=value
                            i-=int(key)
                            break
            else:
                if i<5:
                    result+="IV"
                elif i<10:
                    result+="IX"
                elif i<50:
                    result+="XL"
                elif i<100:
                    result+="XC"    
                elif i<500:
                    result+="CD"
                else:
                    result+="CM"
        return result  