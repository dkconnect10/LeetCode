class Solution:
    def rotate(self, nums, k):
        k=k%len(nums)
        while k>0:
            n=nums.pop()
            nums.insert(0,n)
            k-=1
        