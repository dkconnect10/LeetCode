class Solution:
    def maxSatisfied(self, customers, grumpy, minutes):
        n = len(customers)
        normal = 0
        for i in range(len(customers)):
            if grumpy[i]==0:
                normal+=customers[i]
        temp = 0  
        for i in range(n-minutes+1):
            vmax = 0
            for j in range(i,i+minutes):
                if grumpy[j]==1:
                    vmax+=customers[j]
            temp = max(vmax,temp)
        return normal+temp 