class Solution:
    def searchMatrix(self, matrix, target):

        low=0
        high=len(matrix)-1
        
        while low<=high:
            mid = (low+high)//2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row = matrix[mid]
                start =0
                end = len(row)-1
                
                while start<=end:
                    n = (start+end)//2
                    if row[n]==target:
                        return True
                    elif row[n]>target:
                        end=n-1
                    else:
                        start=n+1
                return False    
            if matrix[mid][-1]<target:
                low=mid+1
            else:
                high=mid-1
        return False            