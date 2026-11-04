class Solution:
    def compareVersion(self, version1, version2):
        v1 = version1.split(".")
        v2 = version2.split(".")

        x = len(v1)
        y = len(v2)
        
        if x>y:
            n = x-y
            for _ in range(n):
                v2.append("0")
        elif x<y:
            n = y-x
            for _ in range(n):
                v1.append("0")
        
        # print(v1,v2)        
        i=0
        while i<len(v1) and i<len(v2):
            if int(v1[i])<int(v2[i]):
                return -1
            elif int(v1[i])>int(v2[i]):
                return 1
            i+=1
        return 0