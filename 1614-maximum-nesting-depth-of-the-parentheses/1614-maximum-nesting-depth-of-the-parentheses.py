class Solution:
    def maxDepth(self, s):
        count=0
        max_depth=0
        for i in s:
            if i=="(":count+=1
            if i==")":count-=1
            if count>max_depth:
                max_depth=count
        return max_depth