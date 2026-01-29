import math

class Solution:
    def hour(self,piles,h):
        total_hour = 0
        for i in range(len(piles)):
            total_hour+=math.ceil(piles[i]/h)
        return total_hour    
   
    def minEatingSpeed(self, piles, h):
        low=1
        high=max(piles)
        ans=float('inf')
       
        while low<=high:
            mid=(low+high)//2
            taking_hour = self.hour(piles,mid)
            if taking_hour<=h:
                if ans>mid:
                   ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans