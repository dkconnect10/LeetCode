class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        freq = {}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        for key,value in freq.items():
            if value==1 and key%2==0:
                return key
        return -1 