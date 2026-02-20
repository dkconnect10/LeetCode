class Solution:
    def firstBadVersion(self, n):
        low = 1
        high = n
        bad = None
        while low<=high:
            mid = (low+high)//2
            
            if isBadVersion(mid)==True:
                bad=mid
                high=mid-1
            else:
                low=mid+1
        return bad            