class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        if len(arr)<2:
            return -1
            
        arrr = set(arr)
        if len(arrr)<2:
            return -1
            
        
        arrr.remove(max(arrr))
        
        return max(arrr)
        
        

