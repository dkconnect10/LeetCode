class Solution:
    def helper(self,candidates, target,i=0,path=None,result=None,s=0):
        if path is None:
            path = []
        if result is None:
            result = []
            
        if s > target:
            return    
        
        if i==len(candidates):
            if s==target:
                result.append(path[:])
            return None
            
        s+=candidates[i]
        path.append(candidates[i])
        self.helper(candidates,target,i+1,path,result,s)
        
        s-=candidates[i]
        path.pop()
        idx=i+1
        while idx<len(candidates) and candidates[idx]==candidates[i]:
            idx+=1
        self.helper(candidates,target,idx,path,result,s)
        
        return result

    def combinationSum2(self, candidates, target):
        candidates.sort()
        return self.helper(candidates,target)
        
        
        