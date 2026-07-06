class Solution:
    def maxVowels(self, s, k):
        vowels = {"a","e","i","o","u"}
        temp = list(s[:k])
        vmax = 0
        count = 0
        for i in temp:
            if i in vowels:
                count+=1
        vmax = max(vmax, count)
        for i in range(k,len(s)):
            val = temp.pop(0)
            if val in vowels:
                count-=1
            temp.append(s[i])
            if s[i] in vowels:
                count+=1
            vmax = max(vmax, count)
        return vmax