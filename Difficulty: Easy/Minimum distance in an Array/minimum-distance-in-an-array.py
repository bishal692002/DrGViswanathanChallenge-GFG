class Solution:
    def minDist(self, arr, x, y):
        if x == y:
            return -1
        
        xx = -1
        yy = -1
        mini = float('inf')
        
        for i in range(len(arr)):
            if x == arr[i]:
                xx = i
            elif y == arr[i]:
                yy = i
            
            if xx != -1 and yy != -1:
                mini = min(mini, abs(yy - xx))
                
        if mini != float('inf'):
            return mini
        
        else:
            return -1
        
        