class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq={}

        for i in s:
            freq[i]=freq.get(i,0)+1

        for i in range(len(s)):
            if freq[s[i]]==1:
                return i
        return -1                     