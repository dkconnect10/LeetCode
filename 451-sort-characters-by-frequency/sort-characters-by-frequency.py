class Solution:
    def frequencySort(self, s):
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
 
        return ''.join(sorted(s, key=lambda x: (-freq[x], x)))