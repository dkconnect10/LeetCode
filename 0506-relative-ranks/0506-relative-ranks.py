class Solution:
    def heapify_down(self,nums,i):
        n = len(nums)
        curr = i

        while True:
            left = curr*2+1
            right = curr*2+2

            if left>=n:
                break
            if right>=n:
                if nums[curr][0]<nums[left][0]:
                    nums[curr],nums[left]=nums[left],nums[curr]
                    curr=left
                else:
                    break
            else:
                if nums[left][0]>nums[right][0]:
                    if nums[curr][0]<nums[left][0]:
                        nums[curr],nums[left]=nums[left],nums[curr]
                        curr=left
                    else:
                        break
                else:
                    if nums[curr][0]<nums[right][0]:
                        nums[curr],nums[right]=nums[right],nums[curr]
                        curr=right
                    else:
                        break    
        return nums   

    def build(self,nums):
        n = len(nums)
        end = n-1
        nonleaf_node = n//2-1
        for i in range(nonleaf_node,-1,-1):
            self.heapify_down(nums,i)
        return nums

    def delete(self,nums):
        nums[0],nums[-1]=nums[-1],nums[0]
        nums.pop()
        self.heapify_down(nums,0)
        return nums

    def findRelativeRanks(self, score):
        heap = []
        result=[""]*len(score)

        for i in range(len(score)):
            heap.append((score[i],i))  
        
        
        self.build(heap)
        rank = 1
        while heap:
            index = heap[0][1]
            
            if rank==1:
                result[index]="Gold Medal"
            elif rank ==2:
                result[index]="Silver Medal"
            elif rank ==3:
                result[index]="Bronze Medal"
            else:
                result[index]=str(rank)
            self.delete(heap)
            rank+=1    
        return result