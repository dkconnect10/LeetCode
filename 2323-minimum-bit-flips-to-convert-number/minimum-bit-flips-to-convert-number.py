class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans = start^goal
        ans=int(ans)
        count=00
        while ans>0:
            if ans%2==1:
                count+=1
            ans = ans//2
        return count
        